# Instrucciones para correr
## Crear world
```
$ export LOCALIZATION=hector_mapping
$ export RVIZ=true
$ export LASER=rplidar
$ roslaunch ca_gazebo create_maze.launch
```
## Explorar
  1. Manualmente
  ```
$ roslaunch ca_tools keyboard_teleop.launch
```
  2. Con algoritmo
```
$ roslaunch ca_mapping_exploration explore_lite.launch
```

## Guardar archivo de mapeo
  ```
$ rosrun map_server map_saver -f <NAME_OF_THE_ENVIRONMENT>
```
( esto genera archivos .pgm y .yaml que levanta el script de cálculo)
## Correr script
  ```
$ rosrun ca_room_sizing gridToSqMeters <NAME_OF_THE_ENVIRONMENT>
```
(se le pasa el nombre de los archivos como parámetro)
