#include <stdio.h>
#include <unistd.h>

int saldo = 1000; // Saldo da conta bancária

// Função que simula a atualização do saldo
void atualiza_saldo(int incremento, int atraso) {
    int saldo_temp = saldo; // Lê o saldo atual
    sleep(atraso); // Simula um atraso diferente para cada "operação"
    saldo_temp += incremento; // Atualiza o saldo temporário
    saldo = saldo_temp; // Escreve o novo saldo
    printf("Novo saldo: %d\n", saldo);
}

int main() {
    printf("Saldo inicial: %d\n", saldo);

    // Simula duas operações de atualização de saldo com atraso diferente
    atualiza_saldo(200, 1); // Atualização 1 com atraso de 1 segundo
    atualiza_saldo(300, 2); // Atualização 2 com atraso de 2 segundos

    printf("Saldo final: %d\n", saldo);
    return 0;
}
