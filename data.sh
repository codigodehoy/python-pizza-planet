#!/bin/sh

declare -A ingredients
declare -A sizes

ingredient_price=( 0 2 1.95 1.35 1 2.15 0.75 1.5 0.85 1.15 0.95)
size_price=( 0 4.5 6 8 11 15)


function insert() {
  local -n array=$1
  for key in ${!array[@]}; do
    echo sqlite3 pizza.sqlite "insert into $2 (name, price) values ('${key}', ${array[${key}]});"
    sqlite3 pizza.sqlite "insert into $2 (name, price) values ('${key}', ${array[${key}]});"
  done
}

function insert_order(){
  for ((i = 0; i < $1; i++)); do
    size_id=$(( $RANDOM % 5 + 1 ))
    echo sqlite3 pizza.sqlite "insert into 'order' (client_name, client_dni, client_address, client_phone, date, total_price, size_id) values ('${clients[$2]}', '$3', '${address[$2]}', '$3', '${dates[$i]}', ${size_price[$size_id]}, $size_id);"
    sqlite3 pizza.sqlite "insert into 'order' (client_name, client_dni, client_address, client_phone, date, total_price, size_id) values ('${clients[$2]}', '$3', '${address[$2]}', '2966548', '${dates[$i]}', ${size_price[$size_id]}, $size_id);"
  done
}


echo "-----------10 Ingredients-----------"
ingredients=( ["mozzarella"]=1.15 ["pepperoni"]=0.85 ["onion"]=0.95 ["extra-cheese"]=1.95 ["chicken"]=1.5 
              ["mushrooms"]=2 ["sausage"]=1.35 ["bacon"]=2.15 ["peppers"]=0.75 ["salami"]=1)

insert ingredients ingredient

echo "-----------5 Size -----------"
sizes=( ["small"]=4.5 ["medium"]=6 ["extra-medium"]=8 ["large"]=11 ["extra-large"]=15)

insert sizes size

echo "-----------50 Orders -----------" 

clients=("David" "Karla" "Santiago" "Freddy" "Veronica" "Domenica" "Cristina" "Joseph" "Alejandra" "Kevin" 
        "Mario" "Sebastian" "Esteban" "Raul" "Israel" "Pedro" "Juan" "Laura" "Mariana" "Marisol"
        "Andres" "Pablo" "Camila" "Tania" "Melani" "Carmen" "Pedro" "Daniel" "Jefferson" "Daniela"
        "Franco" "Marcos" "Ivan" "Jipson" "Wladymir" "Kely" "Claudia" "Dylan" "Fausto" "Katty"
        "Antonio" "Jose" "Messi" "Cristiano" "Mariano" "Lucas" "Ana" "Angie" "Emilio" "Kseniia")

address=("Ajavi" "Atlantico" "San juan" "Calacali" "San jose" "Monjas alto" "Tablon" "El carmen" "Santa ana" "Chillogallo"
        "Tandayapa" "Lloa" "Sarayo" "Oyacachi" "Papallacta" "Nanegal" "Nono" "Chiriboga" "Tambillo" "Mospa"
        "San ramon" "La concordia" "La union" "Pueblito" "Convento" "San isidro" "Luz de america" "Chone" "Baeza" "Cayambe"
        "Jeberos" "Malpuco" "Bretena" "Angamos" "Dalva" "Tauare" "Envira" "Helena" "Deni" "Cayambe"
        "Huigra" "Atlantico" "Mariscal sucre" "Mena" "6 de diciembre" "Solando" "Pintado" "Magdalena" "Cayambe" "La concordia")

dates=("2023-01-25 17:14:26.48690" "2023-01-20 17:14:26.48690" "2023-01-15 13:14:26.48690" "2023-01-25 17:14:26.48690" "2023-01-05 14:14:26.48690" 
      "2023-02-23 17:14:26.48690" "2023-03-12 16:14:26.48690" "2023-03-22 17:14:26.48690" "2022-04-20 19:14:26.48690" "2022-05-15 11:14:26.48690"
      "2023-06-25 17:14:26.48690" "2023-04-25 17:14:26.48690" "2023-02-07 12:14:26.48690" "2023-02-25 17:14:26.48690" "2023-03-18 17:14:26.48690" 
      "2023-01-02 20:14:26.48690" "2023-06-25 17:30:26.48690" "2023-07-25 17:14:26.48690" "2023-08-25 17:14:26.48690" "2023-02-05 18:14:26.48690"
      "2023-10-12 20:14:26.48690" "2023-08-26 17:30:26.48690" "2023-09-25 17:14:26.48690" "2023-10-28 17:14:26.48690" "2023-12-05 13:44:26.48690"
      "2023-03-22 10:14:26.48690" "2023-07-05 17:30:26.48690" "2023-05-21 17:14:26.48690" "2023-06-28 15:14:26.48690" "2023-12-23 16:46:26.48690"
      "2023-08-12 10:14:26.48690" "2023-07-13 17:30:26.48690" "2023-06-14 17:14:26.48690" "2023-05-15 15:14:26.48690" "2023-05-16 16:46:26.48690"
      "2023-03-21 10:14:26.48690" "2023-04-22 17:30:26.48690" "2023-05-23 17:14:26.48690" "2023-06-24 15:14:26.48690" "2023-07-25 16:46:26.48690"
      "2023-03-21 10:14:26.48690" "2023-04-22 17:30:26.48690" "2023-05-23 17:14:26.48690" "2023-06-24 15:14:26.48690" "2023-07-25 16:46:26.48690"
      "2023-01-21 10:14:26.48690" "2023-04-22 17:30:26.48690" "2023-05-23 17:14:26.48690" "2023-06-24 15:14:26.48690" "2023-07-25 16:46:26.48690")


ITER=0
for I in {0..49}
do 
  size_id=$(( $RANDOM % 5 + 1 ))
  echo sqlite3 pizza.sqlite "insert into 'order' (client_name, client_dni, client_address, client_phone, date, total_price, size_id) values (${clients[I]}, $(( $RANDOM * 100000 )), ${address[I]}, '$RANDOM', '$dates', ${size_price[$size_id]}, $size_id);"
  sqlite3 pizza.sqlite "insert into 'order' (client_name, client_dni, client_address, client_phone, date, total_price, size_id) values ('${clients[I]}', '$(( $RANDOM * 100000 ))', '${address[I]}', '$RANDOM', '${dates[I]}', ${size_price[$size_id]}, $size_id);"
  ITER=$(expr $ITER + 1)
done

# The first argument is about number of records and the second indicates the position of the clients list example 'clients[6]'

echo "-----------20 Orders -----------"

insert_order 20 0 $RANDOM

echo "-----------15 Orders -----------"

insert_order 15 6 $RANDOM

echo "-----------15 Orders -----------"

insert_order 15 5 $RANDOM


echo "-----------Order detail -----------"

for I in {1..100}
do
  ingredient_id=$(( $RANDOM % 10 + 1 ))
  echo sqlite3 pizza.sqlite "insert into order_detail ( ingredient_price, order_id, ingredient_id ) values( $ingredient_price, $order_id, $ingredient_id );"
  sqlite3 pizza.sqlite "insert into order_detail ( ingredient_price, order_id, ingredient_id ) values( ${ingredient_price[$ingredient_id]}, $I, $ingredient_id );"
  ITER=$(expr $ITER + 1)
done

echo "-----------Update price -----------"
ITER=0
for I in {1..100}
do
  echo $I
  ingredient_price=$(sqlite3 pizza.sqlite "select ingredient_price from order_detail where order_id = ${I}")
  echo sqlite3 pizza.sqlite "update 'order' set total_price = total_price where _id = '${I}'"
  sqlite3 pizza.sqlite "update 'order' set total_price = total_price + ${ingredient_price}  where _id = '${I}'"
  ITER=$(expr $ITER + 1)
done
