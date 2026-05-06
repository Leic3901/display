execute as @e[tag=sb] run data merge entity @s {transformation:{scale:[1.0,1.0,1.0]}}
execute as @e[tag=sb] store result entity @s transformation.scale[1] float 1 run data get entity @s transformation.scale[0]
execute as @e[tag=sb] store result entity @s transformation.scale[2] float 1 run data get entity @s transformation.scale[0]