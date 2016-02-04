# git-host コマンド

## 機能
4. oauth
5. 鍵類読み込み
3. 引数パース
1. github, bitbucket, gitlab/gitlab.comのリポジトリ一覧を出力

## issue
2. github, bitbucket, gitlab/gitlab.comにリポジトリ作成

## config
~/.githost/config
```
{
  "bitbucket": {
    "consumer": {
      "key": "*****",
      "secret": "*****"
    },
    "defaultuser": "hoge",
    "tokens": {
      "username": {
        "access_token": "****"
        "refresh_token": "****"
        "token_type": "****"
        "expires_in": "****"
      },
      "hoge": {
        "access_token": "****"
      },
      "foo": {
        "access_token": "****"
      }
    }
  },
  "github": {
    "consumer": {
      "key": "*****",
      "secret": "*****"
    },
    "defaultuser": "hoge",
    "tokens": {
    }
  },
  "gitlab": {
    "consumer": {
      "key": "*****",
      "secret": "*****"
    },
    "defaultuser": "hoge",
    "tokens": {
    }
  }
}
```

## ライセンス
Copyright 2016 octaltree

Apache License Version 2.0（「本ライセンス」）に基づいてライセンスされます。あなたがこのファイルを使用するためには、本ライセンスに従わなければなりません。本ライセンスのコピーは下記の場所から入手できます。

http://www.apache.org/licenses/LICENSE-2.0

適用される法律または書面での同意によって命じられない限り、本ライセンスに基づいて頒布されるソフトウェアは、明示黙示を問わず、いかなる保証も条件もなしに「現状のまま」頒布されます。本ライセンスでの権利と制限を規定した文言については、本ライセンスを参照してください。
