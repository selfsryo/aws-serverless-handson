# aws-serverless-handson

[こちら](https://pages.awscloud.com/event_JAPAN_Hands-on-for-Beginners-Serverless-2019_LP.html?trk=aws_introduction_page)をserverless frameworkで実装

## 概要
- リクエストに含まれる日本語を英語に翻訳するAPI
- API Gateway - lambda - AWS translate
- ログはDynamoDBに蓄積

## エンドポイント
`/translate?input_text={}`

## 実行方法
- AWS CLIを設定
- 以下でデプロイ
```shell
sls deploy --aws-profile 任意のプロファイル名
```
- 以下で削除
```shell
sls remove --aws-profile 任意のプロファイル名
```
