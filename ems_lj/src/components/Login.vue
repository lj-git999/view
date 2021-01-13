<template>
  <div id="wrap">
    <div id="top_content">
      <div id="header">
        <div id="rightheader">
          <p>
            2009/11/20
            <br />
          </p>
        </div>
        <div id="topheader">
          <h1 id="title">
            <a href="#">main</a>
          </h1>
        </div>
        <div id="navigation">
        </div>
      </div>
      <div id="content">
        <p id="whereami">
        </p>
        <h1>
          login
        </h1>
        <table cellpadding="0" cellspacing="0" border="0"
               class="form_table">
          <tr>
            <td valign="middle" align="right">
              username:
            </td>
            <td valign="middle" align="left">
              <input v-model="username" type="text" class="inputgri" name="name" />
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              password:
            </td>
            <td valign="middle" align="left">
              <input v-model="password" type="password" class="inputgri" name="pwd" />
            </td>
          </tr>
        </table>
        <p>
          <el-button type="success" class="button" value="Submit" size="small" @click="get_login">登录</el-button>
          &nbsp;&nbsp;
          <router-link to="/register">注册</router-link>
        </p>
      </div>
    </div>
    <div id="footer">
      <div id="footer_bg">
        ABC@126.com
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "Login",
  data(){
    return{
      username:"",
      password:"",
    }
  },
  methods:{
    get_login(){
      this.$axios({
        url:"http://127.0.0.1:8000/userapp/users/",
        method:"get",
        params:{
          username:this.username,
          password:this.password,
        }
      }).then(rst=>{
        console.log(rst.data)
        if (rst.data["message"]){
          let username=rst.data.result['username'];
          sessionStorage.setItem('username',username);
          this.$message.success("恭喜你，登陆成功");
          this.$router.push("/index");
        }
      }).catch(error=>{
        this.$message({
          showClose:true,
          message:"对不起，你输入的用户名或者密码有误",
          type:"error",
          duration:1000,
        })
      })
    }
  }

}
</script>

<style scoped>

</style>
