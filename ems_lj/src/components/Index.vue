<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br />
                        <a href=" " @click="logot">安全退出</a>
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
                    欢迎{{username}}登录
                </h1>
                <table class="table">
                    <tr class="table_header">
                        <td>ID</td>
                        <td>Name</td>
                        <td>Photo</td>
                        <td>Salary</td>
                        <td>Age</td>
                        <td>Operation</td>
                    </tr>
                    <tr class="row1" v-for="emp in emp_list" :key="emp.id">
                        <td>{{emp.id}}</td>
                        <td>{{emp.emp_name}}</td>
                        <td><img :src=emp.full_img style="height: 60px;"></td>
                        <td>{{emp.salary}}</td>
                        <td>{{emp.age}}</td>
                        <td>
                            <a href="javascript:;" @click="delete_emp(emp.id)">删除员工</a>&nbsp;<a href="javascript:;" @click="update_emp(emp.id)">更新员工</a>
                        </td>
                    </tr>
                </table>
                <p>
                    <el-button type="" size="small"><router-link to="/add">增加员工</router-link></el-button>
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
    name: "Index",
    data(){
        return{
            emp_list:[],
            username:'',
        }
    },
    methods:{
        get_show(){
            let username=sessionStorage.getItem("username")
            if (username){
                this.username=username
                this.$axios({
                    url:"http://127.0.0.1:8000/userapp/emps/",
                    method:"get",
                }).then(rst=>{
                    console.log(rst.data);
                    this.emp_list=rst.data;

                }).catch(error=>{
                    console.log(error)
                })
            }else{
                this.message.error("当前用户未登录，请登录");
                this.$router,push('/login');
            }

        },
        update_emp(id){
            this.$router.push("/update/"+id)

        },
        delete_emp(id){
            this.$axios({
                url:"http://127.0.0.1:8000/userapp/emps/"+id+"/",
                method:"delete",
            }).then(rst=>{
                console.log(rst.data);
                this.$router.go(0);
                this.$message({
                    message: '删除成功',
                    type: 'success'
                });
            }).catch(error=>{
                console.log(error)
            })
        },
        logot(){
            sessionStorage.clear()
        }
    },
    created() {
        this.get_show();
    }


}
</script>

<style scoped>

</style>
