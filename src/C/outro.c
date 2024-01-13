#include <stdio.h>

int main()
{
    float numero1, numero2;

    puts("selecione um numero");
    scanf("%f", &numero1);
    puts("outro numero");
    scanf("%f", &numero2);

    if (numero1 > numero2)
    {
        printf("primeiro e maior do que o segundo \n");
    }

    else if (numero1 < numero2)
    {
        printf("segundo numero e maior que o primeiro \n");
    }

    else
    {
        printf("primeiro numero e igual ao segundo \n");
    }
    
    return 0;
}