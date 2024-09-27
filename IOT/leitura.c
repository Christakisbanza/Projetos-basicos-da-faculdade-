#include <SPI.h>  //Biblioteca para utilização do protocolo SPI;


#include <Wire.h>          //Biblioteca para uso do protocolo I2C;
#include <Adafruit_GFX.h>  //Biblioteca para manipulação gráfica no display;


#define OLED_RESET -1  //Em displays que não possuem pino RESET, é dado o valor -1;


#define C_SELECT 10  //Pino SDA do módulo;
#define RESET 9      //Pino RESET do módulo MFRC522;


#define ledVerde 5
#define ledVermelho 4


#define LENGTH(arr) (sizeof(arr) / sizeof((arr)[0]))


#include <MFRC522.h>            //Biblioteca para utilização do circuito RFID MFRC522;
MFRC522 rfid(C_SELECT, RESET);  //Declaração do módulo com o nome "rfid" no sistema com os pinos do define;


#include <Adafruit_SH1106.h>          //Biblioteca para operação do driver de controle do display;
Adafruit_SH1106 display(OLED_RESET);  //Declaração da tela com o nome "display";


byte endereco[4];


String dados = "";  //String vazia para armazenar o endereço da tag/cartão RFID;


unsigned long tempo_anterior = 0;
unsigned long intervalo = 2000;


void setup() {
  Serial.begin(9600);
  display.begin(SH1106_SWITCHCAPVCC, 0x3C);  //Inicialização do display com a biblioteca e endereço de hardware do display;


  SPI.begin();      //Inicialização do protocolo SPI;
  rfid.PCD_Init();  //Inicialização do módulo RFID;
  Serial.println("RFID: Operacional");


  pinMode(ledVerde, OUTPUT);
  pinMode(ledVermelho, OUTPUT);
}


void loop() {
  unsigned long tempo_atual = millis();  //Variável para armazenar o valor da função millis();


  display.clearDisplay();       //Comando para limpar a tela;
  display.setTextColor(WHITE);  //Comando para definir a cor do texto;
  display.setTextSize(1);       //Comando para definir tamanho od




  if (tempo_atual - tempo_anterior >= intervalo) {  //Temporização que faz com que o RFID realize uma leitura a cada 2 seg;
    tempo_anterior = tempo_atual;                   //Variável tempo_anterior sendo "zerada";




    if (!rfid.PICC_IsNewCardPresent()) {  //If para testar caso o módulo NÃO tenha lido nenhum cartão/tag;
      digitalWrite(ledVerde, LOW);
      digitalWrite(ledVermelho, LOW);
      return;
    }
    if (!rfid.PICC_ReadCardSerial()) {  //If para testar caso o módulo NÃO tenha conseguido ler o endereço do cartão/tag;
      return;
    }
  }


  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
    if (endereco[0] != rfid.uid.uidByte[0] || endereco[1] != rfid.uid.uidByte[1] || endereco[2] != rfid.uid.uidByte[2] || endereco[3] != rfid.uid.uidByte[3]) {


      for (int i = 0; i < rfid.uid.size; i++) {
        endereco[i] = rfid.uid.uidByte[i];
      }


      display.setCursor(1, 5);
      display.print("Endereco da TAG (HEX): ");


      for (byte i = 0; i < rfid.uid.size; i++) {  //Loop que percorre o endereço lido no RFID como um vetor;
        if (rfid.uid.uidByte[i] < 0x10) {
          display.print(" 0");
        } else {
          display.print(" ");
        }


        display.print(rfid.uid.uidByte[i], HEX);  //Código para conversão dos dados lidos no módulo, de binário para HEX;


        if (rfid.uid.uidByte[i] < 0x10) {
          dados.concat(String(" 0"));
        } else {
          dados.concat(String(" "));
        }
        dados.concat(String(rfid.uid.uidByte[i], HEX));
      }


      dados.toUpperCase();  //Colocando todos os valores do endereço em caixa alta;
      display.println();    //Printa os valores de endereço no Console Serial;


      if (dados.substring(1) == "A0 79 C2 49") {  //Testa se o endereço lido é igual ao contido entre " ";
        display.println("Acesso Permitido!");
        digitalWrite(ledVerde, HIGH);


        dados = "";  //Zera o valor da string para a próxima leitura;
      } else {
        display.println("Acesso Negado!");
        digitalWrite(ledVermelho, HIGH);


        dados = "";
      }
    }
  }


 


  display.display();  //Mostrar informações na tela;