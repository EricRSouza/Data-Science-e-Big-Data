#!/bin/bash

# Função para baixar e extrair os arquivos
baixaDadosTransp() {
    local diaIni=$1
    local diaFim=$2
    local mes=$3
    local ano=$4

    local dataDir="./dados"
    local tmpDir="./tmp"

    # Criar diretórios, se necessário
    mkdir -p $dataDir
    mkdir -p $tmpDir

    # Percorrer os dias do período
    for dia in $(seq -f "%02g" $diaIni $diaFim); do
        local zipFile="${ano}${mes}${dia}.zip"
        local empenhoFile="${ano}${mes}${dia}_Despesas_Empenho.csv"
        local pagamentoFile="${ano}${mes}${dia}_Despesas_Pagamento.csv"

        echo "Baixando arquivo $zipFile..."
        wget "https://portaldatransparencia.gov.br/download-de-dados/despesas/$zipFile" -O "$tmpDir/$zipFile" 2> /dev/null

        echo "Extraindo arquivos de $zipFile..."
        unzip -o "$tmpDir/$zipFile" "$empenhoFile" "$pagamentoFile" -d "$tmpDir" > /dev/null

        # Concatenar os arquivos
        if [ -f "$tmpDir/$empenhoFile" ]; then
            if [ -f "$dataDir/${ano}${mes}${diaIni}-${diaFim}_Despesas_Empenho.csv" ]; then
                tail -n +2 "$tmpDir/$empenhoFile" >> "$dataDir/${ano}${mes}${diaIni}-${diaFim}_Despesas_Empenho.csv"
            else
                mv "$tmpDir/$empenhoFile" "$dataDir/${ano}${mes}${diaIni}-${diaFim}_Despesas_Empenho.csv"
            fi
        fi

        if [ -f "$tmpDir/$pagamentoFile" ]; then
            if [ -f "$dataDir/${ano}${mes}${diaIni}-${diaFim}_Despesas_Pagamento.csv" ]; then
                tail -n +2 "$tmpDir/$pagamentoFile" >> "$dataDir/${ano}${mes}${diaIni}-${diaFim}_Despesas_Pagamento.csv"
            else
                mv "$tmpDir/$pagamentoFile" "$dataDir/${ano}${mes}${diaIni}-${diaFim}_Despesas_Pagamento.csv"
            fi
        fi

        echo "Limpando arquivo $zipFile..."
        rm -f "$tmpDir/$zipFile"
    done
}

# Verificar se os 4 parâmetros foram fornecidos
if [ "$#" -ne 4 ]; then
    echo "Uso: $0 diaIni diaFim mes ano"
    exit 1
fi

# Chamar a função com os parâmetros fornecidos
baixaDadosTransp "$1" "$2" "$3" "$4"