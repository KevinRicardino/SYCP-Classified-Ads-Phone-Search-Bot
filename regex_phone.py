import re

# Regex para celular brasileiro (DDD + 9 + 8 dígitos)
PHONE_REGEX = re.compile(
    r"\(?0?([1-9]{2})[ \-\.\)]{0,2}?(9[ \-\.]?)(\d{4})[ \-\.\)]?(\d{4})"
)

text = """
whatsapp 16 98129 2312
(34) 99999-6666
011 99898.2323
tel:11.98988.1122

Se possivel chamar no whats 15 996163537 , chat demoro pouco para responder

15 9 2827 2312

Se possivel chamar no whats 15996163537

📞 Contatos adicionais:
Whats: (21) 98765-4321
Telefone 21 99876 5432
Cel: 21998765432
Contato: 0(31) 91234-5678
Chamar no WhatsApp 31.9.8765.4321
Tel 41 99888-7777
Whatsapp: 0 41 9 9888 7777
Número alternativo 48991234567
Falar com João: (48) 9 9123 4567
Whats comercial: 11987654321
Telefone SP: 11 9 8765-4321
Atendimento: (62)99876.1111

Completo
4 pneus novos
Com garantia e Procedencia
Todos os veículos são periciados!
"""

print("📱 Telefones encontrados (por grupo):\n")

for match in PHONE_REGEX.finditer(text):
    ddd = match.group(1)
    nove = match.group(2)
    parte1 = match.group(3)
    parte2 = match.group(4)

    print(f"DDD: {ddd}")
    print(f"9º dígito: {nove}")
    print(f"Número: {parte1}-{parte2}")
    print(f"{ddd} {nove} {parte1} {parte2}")

    print("-" * 30)