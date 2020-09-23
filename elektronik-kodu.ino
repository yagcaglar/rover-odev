int motor_yon[4];
int motor_hiz[4];
char str[19];
char temp[4];
void setup()
{
  Serial.begin(9600);
  randomSeed(analogRead(A0));

  str[0]='S';
  str[17]='F';
  
  for(int i=0;i<4;i++){ //motorların yön ve hız değerlerini belirleyen 8 sayı oluşturulur.
   	motor_yon[i]=random(0,2);
    motor_hiz[i]=random(0,256);
  }
  
  int k=0;
  
  for(int i=0;i<4;i++){
    itoa(motor_yon[i],temp,10);
    str[++k]=temp[0]; //motorun yönü girilir.
    
    //motorun basamak sayısına göre başında sıfır olacak şekilde hiz değerleri girilir.
    
    if(motor_hiz[i]>=100){
     	itoa(motor_hiz[i],temp,10);
     	for(int j=0;j<3;j++){
       	str[++k]=temp[j]; 
     	}
    }
    else if(motor_hiz[i]>=10){
      str[++k]='0';
     	itoa(motor_hiz[i],temp,10);
     	for(int j=0;j<2;j++){
       	str[++k]=temp[j]; 
      	}
    }
    else{
    	str[++k]='0';
     	str[++k]='0';
     	itoa(motor_hiz[i],temp,10);
     	str[++k]=temp[0];
    }
  }
  
  Serial.println(str);
}

void loop()
{
}
