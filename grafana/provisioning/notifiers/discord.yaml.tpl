# config file version
apiVersion: 1

notifiers:
  - name: FreezerTemp
    type: discord
    is_default: true
    uid: notifier1
    settings:
      autoResolve: true
      content: ""
      httpMethod: "POST"
      severity: "critical"
      uploadImage: true
      url: "<URL>"
