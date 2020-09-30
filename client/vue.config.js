/* eslint-disable @typescript-eslint/no-var-requires */
const path = require("path");
//const CompressionPlugin = require("compression-webpack-plugin");

module.exports = {

  outputDir: path.resolve(__dirname, "../server/dist"),
  assetsDir: "static",
  indexPath: "index.html",
  lintOnSave: false,
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:5000/",
        changeOrigin: true
      }
    }
  },
  configureWebpack: {
    devtool: "source-map"
  }
};
