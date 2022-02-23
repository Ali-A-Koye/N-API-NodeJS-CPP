{
  "targets": [
    {
      "target_name": "main",
      "sources": [ "main.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}