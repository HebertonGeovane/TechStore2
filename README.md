# 🛒 TechStore | Projeto Final AWS re/Start

## Sobre o Projeto

**TechStore** é uma cadeia fictícia de lojas voltadas para o comércio de tecnologia. Como parte dessa cadeia, temos a **TechShop**, um e-commerce moderno que oferece produtos eletrônicos com entrega rápida e segura. 

Este projeto foi desenvolvido com o objetivo de aplicar os conhecimentos adquiridos ao longo do curso **AWS re/Start**, simulando um cenário real de implantação de uma aplicação web escalável, segura e altamente disponível na AWS.

---

##  Objetivo Educacional

O projeto é **100% educacional**, desenvolvido como **Trabalho de Conclusão de Curso (TCC)** do programa AWS re/Start. Ele visa consolidar conhecimentos práticos em infraestrutura cloud, automação e alta disponibilidade usando os serviços da AWS.

##  Tecnologias Utilizadas

### 🔸 ☁️ AWS

[![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)]()
[![EC2](https://img.shields.io/badge/Amazon%20EC2-FF9900?style=for-the-badge&logo=amazon-ec2&logoColor=white)]()
[![RDS](https://img.shields.io/badge/Amazon%20RDS-527FFF?style=for-the-badge&logo=amazon-rds&logoColor=white)]()
[![Lambda](https://img.shields.io/badge/AWS%20Lambda-F47FFF?style=for-the-badge&logo=aws-lambda&logoColor=white)]()
[![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=for-the-badge&logo=amazon-cloudwatch&logoColor=white)]()
[![SNS](https://img.shields.io/badge/SNS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)]()
[![IAM](https://img.shields.io/badge/IAM-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)]()

---

### 🧰 Outras Tecnologias

[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=yellow)]()
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)]()
[![MySQL](https://img.shields.io/badge/MySQL-00758F?style=for-the-badge&logo=mysql&logoColor=white)]()
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)]()
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)]()
[![Amazon Linux](https://img.shields.io/badge/Amazon%20Linux-232F3E?style=for-the-badge&logo=linux&logoColor=white)]()

---

## 🧱 Arquitetura na AWS

A arquitetura do projeto TechStore foi cuidadosamente planejada para refletir boas práticas da AWS em termos de:

- **Segurança**
- **Alta disponibilidade**
- **Escalabilidade**
- **Custo eficiente**

### Componentes:

- **VPC Personalizada (TechStore-VPC)**  
  - CIDR: `10.0.0.0/16`

- **Sub-redes**  
  - 🌐 **Públicas**: Hospedam instâncias EC2 para aplicação Flask  
  - 🔐 **Privadas**: Hospedam banco de dados RDS (MySQL)

- **Zonas de Disponibilidade**
  - Duas AZs: `us-east-1a` e `us-east-1b`
  - **Multi-AZ** para resiliência

- **Load Balancer (ALB)**  
  - Distribui o tráfego entre as instâncias EC2

- **Auto Scaling Group**  
  - Garante que a aplicação seja automaticamente restaurada em caso de falhas

- **Amazon RDS (MySQL)**  
  - Banco de dados gerenciado em sub-rede privada
  - Alta disponibilidade com Multi-AZ

- **Amazon CloudWatch**
  - Monitoração de instâncias, ALB e RDS
  - Dashboard customizado com métricas em tempo real

- **SNS + Lambda**
  - Função Lambda para simular falhas
  - SNS para envio de alertas

---

## 📌 O que os alunos precisam desenvolver

Para concluir o projeto com sucesso, os alunos devem:

1. Criar a infraestrutura de rede (VPC, sub-redes, route tables, IGW, etc.)
2. Criar e configurar uma **instância EC2** com Flask conectada ao RDS
3. Criar uma **imagem AMI** da instância para uso no **Auto Scaling Group**
4. Configurar um **Launch Template + Auto Scaling Group**
5. Criar um **Load Balancer** que escute na porta 5000
6. Implantar a aplicação e garantir acesso via ALB
7. Criar **uma função Lambda** para simular falhas da instância
8. Configurar **SNS** para enviar notificações via e-mail
9. Montar um **Dashboard no CloudWatch** com métricas chave do ambiente
10. Fazer um teste completo de failover e recuperação automática da aplicação

### 📘 Guia Passo a Passo (Notion)

Acesse o guia completo com o passo a passo do projeto clicando no link abaixo:

👉 [Clique aqui para acessar o guia do projeto no Notion](https://www.notion.so/seunome/TechStore-Passo-a-Passo-123abc456def)
---

## 🧰 Tecnologias e Serviços AWS Utilizados

| Serviço           | Descrição                                    |
|-------------------|-----------------------------------------------|
| `Amazon VPC`      | Rede virtual com sub-redes públicas e privadas |
| `Amazon EC2`      | Instância de aplicação Flask                  |
| `Amazon RDS`      | Banco de dados MySQL em alta disponibilidade |
| `Elastic Load Balancer (ALB)` | Balanceamento de carga da aplicação  |
| `Auto Scaling`    | Escalabilidade e failover automático          |
| `Amazon CloudWatch` | Monitoramento e Dashboard                    |
| `AWS Lambda`      | Automatização de falhas simuladas             |
| `Amazon SNS`      | Notificações de eventos críticos              |
| `IAM`             | Gerenciamento de permissões e políticas       |

---

## 🧑‍🏫 Projeto criado por

👨‍🏫 **Heberton Geovane**  
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hebertong/)

---

## 📷 Screenshots e Diagramas

> ⚠️ Sugerido: Adicione aqui screenshots do CloudWatch Dashboard, arquitetura da VPC e o site da TechShop rodando. Diagramas com [Lucidchart](https://www.lucidchart.com/) ou [draw.io](https://draw.io) deixam o projeto mais profissional.

---

## 📝 Licença

Este projeto é livre para fins educacionais.  
Não utilizar para fins comerciais sem autorização.

---

## 💡 Dica Final

Se você concluiu esse projeto, parabéns!  
Você aplicou conhecimentos reais de arquitetura AWS dignos de um ambiente de produção. 🚀


