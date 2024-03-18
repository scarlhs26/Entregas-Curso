<?php 
/*
EJERCICIOS SECCION 1.

1) Calcular e imprimir el area de un rectangulo.
2) Verficar si un numero es par o impar.
3) Comprobar si un estudiante aprobo o reprobo un examen.
4) Calcular e impimir la circunferencia de un circulo.
5) Determinar si un year es bisiesto o no.
6) Determinar la estacion del year segun un mes. (por numero de mes).

*/


//1) 
$ancho = 5;
$alto = 10;

$area = ($ancho * $alto)/2;
echo '<br>'.'El area del rectangulo es: ' . $area;


//2)
$num = 5;

if($num % 2 == 0){
    echo '<br>'. 'El numero ' . $num . ' es par';
}else{
    echo '<br>'. 'El numero ' . $num . ' es impar';
}

//3)

$nota = 5;

if($nota >= 7){
    echo '<br>'. 'Aprobaste';
}else{
    echo '<br>'. 'Reprobaste';
}

//4)

$r = 5;

$curcunferencia = 2* $r * 3.14;
echo '<br>'. 'La circunferencia del circulo es: ' . $curcunferencia;

//5)

$year = 2024;

if($year % 4 == 0){
    echo '<br>'. 'El año ' . $year . ' es bisiesto';
    
}else{
    echo '<br>'. 'El año ' . $year . ' no es bisiesto';
}

//6)

$mes = 'Junio';

switch ($mes) {
    case 'marzo':
    case 'abril':
    case 'mayo':
    case 'junio':
        echo "Primavera";
        break;
    case 'julio':
    case 'agosto':
    case 'septiembre':
        echo "Es verano";
        break;
    case 'octubre':
    case 'noviembre':
    case 'diciembre':
        echo "Es otoño";
        break;
    default:
        echo "Es invierno";
        break;
}




?>