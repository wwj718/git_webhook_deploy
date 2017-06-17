# git webhook deploy
简答的自动化部署脚本，利用git webhook触发


# 部署
gunicorn -w 4 -b 127.0.0.1:5005 git_webhook_server:app
