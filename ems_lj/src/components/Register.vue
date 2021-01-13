<template>
  <div id="wrap">
    <div id="top_content">
      <div id="header">
        <div id="rightheader">
          <p>
            2009/11/20
            <br/>
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
          注册
        </h1>
        <table cellpadding="0" cellspacing="0" border="0"
               class="form_table">
          <tr>
            <td valign="middle" align="right">
              用户名:
            </td>
            <td valign="middle" align="left">
              <input v-model="username" type="text" class="inputgri" name="username"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              真实姓名:
            </td>
            <td valign="middle" align="left">
              <input v-model="re_name" type="text" class="inputgri" name="name"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              密码:
            </td>
            <td valign="middle" align="left">
              <input v-model="password" type="password" class="inputgri" name="pwd"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              确认密码:
            </td>
            <td valign="middle" align="left">
              <input v-model="re_password" type="password" class="inputgri" name="pwd"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              性别:
            </td>
            <td valign="middle" align="left">
              男
              <input type="radio" class="inputgri" name="sex" value="0" checked="checked"/>
              女
              <input type="radio" class="inputgri" name="sex" value="1" @click="checked"/>
            </td>
          </tr>

        </table>
        <p>
          <el-button type="success" @click="btn">注册</el-button>
          <router-link to="/login">已有账号，去登录</router-link>

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
  name: "Register",
  data(){
    return{
      username:"",
      re_name:"",
      password:"",
      re_password:"",
      sex:0,
    }
  },
  methods:{
    btn(){
      if (this.re_password === this.password){
        this.$axios({
          url:"http://127.0.0.1:8000/userapp/users/",
          method:'post',
          data:{
            username:this.username,
            re_name:this.re_name,
            password:this.password,
            re_password:this.re_password,
            sex:this.sex,
          }
        }).then(rst=>{
          console.log(rst.data);
          if (rst.status === 201){
            this.$router.push('/login');
          }
        }).catch(error=>{
          console.log(error);
          this.$message.error("用户注册信息填写错误");
        })
      }else{
        this.$message.error("确认密码错误")
      }

    },
    checked(){
      this.sex=1
    }
  }

}
</script>

<style scoped>

</style>
