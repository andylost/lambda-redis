# lambda-redis

Exemplo criado para pegar dados de um arquivo e salvar no redis.

## Serverless 

Para instalação do [Serverless](https://serverless.com/framework/docs/providers/aws/guide/installation/) clicar o link e seguir o passo a passo.


## AWS CLI

Seguir o manual de instalação do [cli](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-install.html) e após a instalação configurar o [aws config](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-configure.html)

Para utilização do AWS CLI via serverless precisamos das chaves de acesso.
Exemplo abaixo:

```cmd
aws configure --profile user2
AWS Access Key ID [None]: AKIAI44QH8DHBEXAMPLE
AWS Secret Access Key [None]: je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY 
Default region name [None]: us-east-1 
Default output format [None]: json
```

## Referencias do  serverless.yml

Toda documentação de referencia está [aqui](https://serverless.com/framework/docs/providers/aws/guide/serverless.yml/)

    serverless deploy --stage dev --verbose

o comando stage faz referencia ao ambiente que iremos fazer o deploy.
`dev`, `hml` e `prd`.