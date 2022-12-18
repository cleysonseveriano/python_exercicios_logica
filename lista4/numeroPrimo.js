let N = parseInt(prompt())
while(N > 0){
    const X = parseInt(prompt())
    let somatorio = 0
    for(let i = 1; i < X+1; i++ ){
        if(X%i==0){
            somatorio = somatorio + 1
        }
    }
    if(somatorio==2){
        console.log(`${X} eh primo`)
    } else{
        console.log(`${X} nao eh primo`)
    }
    N = N -1
}