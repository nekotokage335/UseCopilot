# 1.概要
Copilotの質問したいことをファイルに書いて、RequestCopilot.pyを実行すると、自動で質問を行ってくれます。 
 
具体的には以下のような動きです。 
* data/input.txtに質問したいことを書きます。質問したいことが複数個ある場合は改行して書きます。(1行につき1個の質問を書く形です。)
* RequestCopilot.pyを実行するとdata/input/input.txtの質問を読み取り、1行ずつCopilotに送信していきます。Copilotへの送信は、Seleniumを使用してGoogleChromeを操作することで実行されます。
* Copilotからの返答はdata/output/output_yyyymmddss.txtに記録されます。(yyyymmddssはRequestCopilot.pyが実行された時間が入ります。)

# 2.前提となる環境
正常に動作することを確認できた環境の内容は、以下のとおりです。
* OS：Windows11
* Python：3.11.9
* Selenium：4.21.0

# 3.準備方法及び使い方
* Pythonをインストールしていない場合は、インストールしてください。
* PowerShell又はコマンドプロンプトを開き、以下のコマンドを実行してSeleniumをインストールしてください。
  
  `pip install selenium==4.21.0`
* このリポジトリをZIPでダウンロードしてください。ダウンロードしたZIPはデスクトップ配下に「copilot」というフォルダ名で解凍/展開してください。
* <デスクトップのパス>\copilot\data\input\input.txtを開き、Copilotに質問したいことを書いてください。質問したいことが複数個ある場合は改行して書きます。(1行につき1個の質問を書く形です。)
* PowerShell又はコマンドプロンプトを開き、以下のコマンドを実行してRequestCopilot.pyを実行してください。 

  `python <デスクトップのパス>/copilot/RequestCopilot.py`
* 実行が完了するのを待ってください。1つの質問につき約1分ほどかかります。
* <デスクトップのパス>\copilot\data/output/output_yyyymmddss.txtを確認し、Copilotからの返答を確認してください。(yyyymmddssはRequestCopilot.pyが実行された時間が入ります。)

# 4.補足
* GoogleChrome及びChromeDriverがインストールされていない場合は、RequestCopilot.py実行時に自動でインストールされます。(インストールされる場所はC:\Users\<ユーザー名>\.cache\seleniumです。)
