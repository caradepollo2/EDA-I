Funcion cifrado <- cesar(f,c)
	definir abc,cifrado,decifrado Como Caracter;
	Definir i,j,k Como Entero;
	Dimension abc[26];
	cifrado <- "";
	
	
	abc[0]<- "a";
	abc[1]<- "b";
	abc[2]<- "c";
	abc[3]<- "d";
	abc[4]<- "e";
	abc[5]<- "f";
	abc[6]<- "g";
	abc[7]<- "h";
	abc[8]<- "i";
	abc[9]<- "j";
	abc[10]<-"k";
	abc[11]<-"l";
	abc[12]<-"m";
	abc[13]<-"n";
	abc[14]<-"o";
	abc[15]<-"p";
	abc[16]<-"q";
	abc[17]<-"r";
	abc[18]<-"s";
	abc[19]<-"t";
	abc[20]<-"u";
	abc[21]<-"v";
	abc[22]<-"w";
	abc[23]<-"x";
	abc[24]<-"y";
	abc[25]<-"z";
	
	Para i <- 0 Hasta (Longitud(f)-1) Con Paso 1 Hacer
		Si (Subcadena(f,i,i) = " ") Entonces
			cifrado <- Concatenar(cifrado," ");
		Sino
			Para j<-0 Hasta 25 Con paso 1 Hacer
				Si (Subcadena(f,i,i) = abc[j]) Entonces
					Si ((j+c)>25) Entonces
						k<-((j+c)-26);
					Sino
						k<-j+c;
					FinSi
					cifrado <- Concatenar(cifrado,abc[k]);
				FinSi
			FinPara
		FinSi
	FinPara
	
FinFuncion



Proceso cifrar
	Definir frase Como Caracter;
	Definir x Como Entero;
	
	Escribir "Ingrese Frase a cifrar";
	Leer frase;
	Escribir "Ingrese desplazamiento del cifrado";
	Leer x;
	Limpiar Pantalla;
	frase <-minusculas(frase);
	
	
	Si (x > 26) Entonces
		Escribir "El corrimiento no puede ser mayor a 26";
	Sino
		Escribir "La frase: ´´",frase, "´´ es: ",cesar(frase,x);
	FinSi;
FinProceso