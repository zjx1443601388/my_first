#ip转整型
function ip2int(){
    A=$(echo $1 | cut -d '.' -f1)
    B=$(echo $1 | cut -d '.' -f2)
    C=$(echo $1 | cut -d '.' -f3)
    D=$(echo $1 | cut -d '.' -f4)
    result=$(($A<<24|$B<<16|$C<<8|$D))
    echo $result
}
#整型转IP
function int2ip(){
    A=$((($1 & 0xff000000 ) >>24))
    B=$((($1 & 0x00ff0000)>>16))
    C=$((($1 & 0x0000ff00)>>8))
    D=$(($1 & 0x000000ff))
    result=$A.$B.$C.$D
    echo $result
}