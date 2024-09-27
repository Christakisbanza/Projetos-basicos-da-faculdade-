#include <LiquidCrystal.h>

#define BUTTON 2
#define BUTTON2 3

#define DB7 8
#define RS 7
#define E 6
#define DB4 5
#define DB5 4
#define DB6 9

#define BTN3 12 
#define BTN5 13

LiquidCrystal tela (RS, E, DB4, DB5, DB6, DB7);

// Dados do relógio 
int seg = 0;
int min = 0;
int hora = 0;

// Dados do cronometro 
int segCrono = 0;
int minCrono = 0;
int horaCrono = 0;

// Dados do cronometro atualizado
int segAtual = 0;
int minAtual = 0;
int horaAtual = 0;

volatile bool flag = false;

// Booleano que gerencia a parado do cronometro
volatile bool parar = true;

// Booleano que permite a zerar o cronometro
volatile bool zerar = false;

// Booleano que libera a contagem do cronometro
volatile bool liberaContagem = false;


void setup() {
  tela.begin(16, 2);
  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(BUTTON2, INPUT_PULLUP);
  pinMode(BTN3, INPUT_PULLUP);
  pinMode(BTN5, INPUT_PULLUP);
  
  tela.clear();
  tela.setCursor(4, 0);
  tela.print("Relogio :");
  
  uiContagem();
	
  attachInterrupt(digitalPinToInterrupt(BUTTON2),isr2, RISING);
  attachInterrupt(digitalPinToInterrupt(BUTTON), isr, RISING);
}

void isr() {
  flag = true;
  liberaContagem = false;
}

void isr2(){
  parar = false;
  zerar = false;
  liberaContagem = true;
}

// Fução responsavel por zerar o valor do cronometro
void zerarValores(){
  tela.clear();
  
  segCrono = 0;
  minCrono = 0;
  horaCrono = 0;
  
  segAtual = 0;
  minAtual = 0;
  horaAtual = 0;
  
  tela.setCursor(2, 0);
  tela.print("Cronometro :");
  
  if(zerar == true){
    if(segAtual < 10){
      tela.setCursor(11, 1);
      tela.print(0);
      tela.print(0);
    }else{
      tela.setCursor(11, 1);
      tela.print(0);
    }
    if(minAtual < 10){
      tela.setCursor(7, 1);
      tela.print(0);
      tela.print(0);
    }else{
      tela.setCursor(7, 1);
      tela.print(0);
    }
    if(horaAtual < 10){
      tela.setCursor(3, 1);
      tela.print(0);
      tela.print(0);
    }else{
      tela.setCursor(3, 1);
      tela.print(0);
    }
  }

}

// Função que deixa o cronometro parado com os valores atualizados
void cronometro() {
  tela.clear();
  
  tela.setCursor(2, 0);
  tela.print("Cronometro :");
  
   
  if (segAtual < 10){
    tela.setCursor(11 , 1);
    tela.print(0);
    tela.print(segAtual);
  }else{
    tela.setCursor(11 , 1);
    tela.print(segAtual);
  }
  
  if (minAtual < 10) {
    tela.setCursor(7, 1);
    tela.print(0);
    tela.print(minAtual);
  }else{
    tela.setCursor(7, 1); 
    tela.print(minAtual);
  }
  
  if(horaAtual < 10){
    tela.setCursor(3, 1);
    tela.print(0);
    tela.print(horaAtual);
  }else{
    tela.setCursor(3, 1);
    tela.print(horaAtual);
  }
  
  if(parar == true){
    if(segAtual < 10){
      tela.setCursor(11, 1);
      tela.print(0);
      tela.print(segAtual);
    }else{
      tela.setCursor(11, 1);
      tela.print(segAtual);
    }
    if(minAtual < 10){
      tela.setCursor(7, 1);
      tela.print(0);
      tela.print(minAtual);
    }else{
      tela.setCursor(7, 1);
      tela.print(minAtual);
    }
    if(horaAtual < 10){
      tela.setCursor(3, 1);
      tela.print(0);
      tela.print(horaAtual);
    }else{
      tela.setCursor(3, 1);
      tela.print(horaAtual);
    }
  }
}

// Funçao que inicia a comtagem do cronometro
void cronometroConta(){
  
  if (segCrono < 10){
    tela.setCursor(11 , 1);
    tela.print(0);
    tela.print(segCrono);
  }else{
    tela.setCursor(11 , 1);
    tela.print(segCrono);
  }
  
  if (minCrono < 10) {
    tela.setCursor(7, 1);
    tela.print(0);
    tela.print(minCrono);
  }else{
    tela.setCursor(7, 1); 
    tela.print(minCrono);
  }
  
  if(horaCrono < 10){
    tela.setCursor(3, 1);
    tela.print(0);
    tela.print(horaCrono);
  }else{
    tela.setCursor(3, 1);
    tela.print(horaCrono);
  }
  
  if (parar == false && zerar == false){
    for (segCrono = 0; segCrono <= 60; segCrono++) {
      delay(10);
      
      if (segCrono < 10){
        tela.setCursor(11 , 1);
        tela.print(0);
        tela.print(segCrono);
      }else{
        tela.setCursor(11 , 1);
        tela.print(segCrono);
      }

      if (segCrono == 60) {
        segCrono = 0;
        minCrono++;
        if (minCrono < 10) {
          tela.setCursor(7, 1);
          tela.print(0);
          tela.print(minCrono);
        }else{
          tela.setCursor(7, 1); 
          tela.print(minCrono);
        }
      } else if (minCrono == 60) {
        minCrono = 0;
        horaCrono++;
        if(horaCrono < 10){
          tela.setCursor(3, 1);
          tela.print(0);
          tela.print(horaCrono);
        }else{
          tela.setCursor(3, 1);
          tela.print(horaCrono);
        }
      }
      segAtual = segCrono;
      minAtual = minCrono;
      horaAtual = horaCrono;
      
      int estadoBTN3 = digitalRead(BTN3);
      
      if(estadoBTN3 == 0){
        cronometro();
        parar = true;
        return;
      }
      
      int estadoBTN5 = digitalRead(BTN5);
      
      if(estadoBTN5 == 0){
        zerar = true;
        zerarValores();
        return ;
      }
    }
  }
}

// Funçao do loop
void loop() {
  int estadoBT = digitalRead(BUTTON);
  int estadoBT2 = digitalRead(BUTTON2);
  
 
  
    for (seg = 0; seg <= 60; seg++) {
      delay(1000);
      
      if(seg < 10){ 
        tela.setCursor(12, 1);
        tela.print(0);
        tela.print(seg);
      }else{
        tela.setCursor(12, 1);
        tela.print(seg);
      }
      
      
      if (flag == true) {
        cronometro();
        
        if(parar == false && liberaContagem == true){
        	cronometroConta();
      	}
      }
      
      
      int estadoBTN5 = digitalRead(BTN5);
      
      if(estadoBTN5 == 0){
        zerar = true;
        zerarValores();
        return ;
      }
     
      

      if (seg == 60) {
        seg = 0;
        min++;
        if(min < 10){
          tela.setCursor(8, 1);
          tela.print(0);
          tela.print(min);
        }else{
          tela.setCursor(8, 1);
          tela.print(min);
        }  

      } else if (min == 60) {
        min = 0;
        hora++;
        if(hora < 10){
          tela.setCursor(4, 1);
          tela.print(0);
          tela.print(hora);
        }else {
          tela.setCursor(4, 1);
          tela.print(hora);
        }
      }
    
  }
}
// Funçao que armazena os valores a serem printados em determinado momento
void uiContagem(){
  tela.setCursor(4, 1);
  tela.print(0);
  tela.print(hora);

  tela.setCursor(8, 1);
  tela.print(0);
  tela.print(min);

  tela.setCursor(12, 1);
  tela.print(0);
  tela.print(seg);
  
}
