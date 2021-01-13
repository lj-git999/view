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
                        <a href="#">Main  欢迎{{username}}！</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    add Emp info:
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            name:
                        </td>
                        <td valign="middle" align="left">
                            <input v-model="emp_name" type="text" class="inputgri" name="name"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            photo:
                        </td>
                        <td valign="middle" align="left">
                            <input ref="img" type="file" name="photo"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            salary:
                        </td>
                        <td valign="middle" align="left">
                            <input v-model="salary" type="text" class="inputgri" name="salary"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            age:
                        </td>
                        <td valign="middle" align="left">
                            <input v-model="age" type="text" class="inputgri" name="age"/>
                        </td>
                    </tr>
                </table>
                <p>
                    <el-button type="success" class="button" value="Confirm" size="mini" @click="add_emp">确认添加
                    </el-button>
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
    name: "Add_emp",
    data() {
        return {
            emp_name: '',
            salary: "",
            img: "",
            age: "",
            username: ''
        }
    },
    methods: {
        add_emp() {
            let formDate = new FormData();
            formDate.append("emp_name", this.emp_name)
            formDate.append("salary", this.salary)
            formDate.append("img", this.$refs.img.files[0])
            formDate.append("age", this.age)
            this.$axios({
                url: "http://127.0.0.1:8000/userapp/emps/",
                method: "post",
                data: formDate,
                headers: {
                    "content-type": "multipart/form-data"
                },
            }).then(rst => {
                console.log(rst.status);
                if (rst.status === 201) {
                    this.$router.push("/index");
                }
            }).catch(error => {
                console.log(error)
            })
        }

    }

}
</script>

<style scoped>

</style>
