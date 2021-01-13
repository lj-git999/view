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
                        <a href="#">Main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    update Emp info:
                </h1>
                <form action="emplist.html" method="post" :model="emp_list">
                    <table cellpadding="0" cellspacing="0" border="0"
                           class="form_table">
                        <tr>
                            <td valign="middle" align="right">
                                id:
                            </td>
                            <td valign="middle" align="left">
                                {{ emp_list.id }}
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                name:
                            </td>
                            <td valign="middle" align="left">
                                <input v-model="emp_list.emp_name" type="text" class="inputgri" name="name" value="zhangshan"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                photo:
                            </td>
                            <td valign="middle" align="left">
                                <input ref="img" type="file" name="photo" />
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                salary:
                            </td>
                            <td valign="middle" align="left">
                                <input v-model="emp_list.salary" type="text" class="inputgri" name="salary" value="20000"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                age:
                            </td>
                            <td valign="middle" align="left">
                                <input v-model="emp_list.age" type="text" class="inputgri" name="age" value="20"/>
                            </td>
                        </tr>
                    </table>
                    <p>
                        <el-button type="success" class="button" value="Confirm" size="mini" @click="update_emp">提交更新</el-button>
                    </p>
                </form>
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
    name: "Update",
    data(){
        return{
            emp_list:{
                id:'',
                emp_name:'',
                age:"",
                salary:"",
            }
        }
    },
    methods:{
        update_emp(){
            let id = this.$route.params.id
            let formDate=new FormData();
            formDate.append("emp_name",this.emp_list.emp_name)
            formDate.append("salary",this.emp_list.salary)
            formDate.append("age",this.emp_list.age)
            this.$axios({
                url:"http://127.0.0.1:8000/userapp/emps/"+id+"/",
                method:'patch',
                data:formDate,
            }).then(rst=>{
                console.log(rst.status);
                if (rst.status === 200){
                    this.$router.push('/index')
                }
            }).catch(error=>{
                console.log(error)
            })


        },
        get_update(){
            let username=sessionStorage.getItem('username');
            if (username){
                let id = this.$route.params.id
                console.log(id)
                this.$axios({
                    url:"http://127.0.0.1:8000/userapp/emps/"+id+"/",
                    method:"get",
                }).then(rst=>{
                    console.log(rst.data);
                    this.emp_list=rst.data
                }).catch(error=>{
                    console.log(error);
                })
            }else{
                this.$message.error('当前用户未登录，请登录');
                this.$router.push('/login')
            }
        }
    },
    created() {
        this.get_update();
    }
}
</script>

<style scoped>

</style>
