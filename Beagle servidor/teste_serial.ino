//######################## DECLARAÇÕES ############################

String leStringSerial();
int le_entrada();

int led = 13;
int i = 0;
  
void setup() { 
 pinMode(led, OUTPUT); 
 Serial.begin(9600);
}


//######################################################
void loop() {
  Serial.write("testando a comunicacao");
  delay(5000);
  
  // Se receber algo pela serial
  if (Serial.available() > 0)
  {
    // Lê toda string recebida
    String recebido = leStringSerial();
    if (recebido == "Teste")
    {
        Serial.write("Comunicacao OK!\n");
    }
    if (recebido == "BBG ACK!")
    {
        Serial.write("Ardo ACK"); 
    }
  }
}
//##################### FUNÇÔES ##################################
  
//Função que lê uma string da Serial e retorna-a  
String leStringSerial(){
  String conteudo = "";
  char caractere;
  
  // Enquanto receber algo pela serial
  while(Serial.available() > 0) {
    // Lê byte da serial
    caractere = Serial.read();
    // Ignora caractere de quebra de linha
    if (caractere != '\n'){
      // Concatena valores
      conteudo.concat(caractere);
    }
    // Aguarda buffer serial ler próximo caractere
    delay(10);
  }
    
  Serial.print("Recebi: ");
  Serial.println(conteudo);
  Serial.print(" ");
    
 return conteudo;
}

//Função que monitora a entrada

int le_entrada(int pino){
  if (pino == 1)
    return 1;
  else
    return 0;
}
