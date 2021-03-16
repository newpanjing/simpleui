Vue.component('sub-menu', {
    props: ['menus', 'fold'],
    methods: {
        openTab(data) {
            window.app.openTab(data);
        }
    },
    template: `
        <div>
        <template v-for="(item,i) in menus" :key="item.eid">
                <el-menu-item v-if="!item.models" :index="item.eid+''" @click="openTab(item,item.eid)">
                    <i :class="item.icon"></i>
                    <span v-if="!fold" slot="title" v-text="item.name"></span>
                </el-menu-item>
    
                <el-submenu v-else :index="item.eid+''">
                    <template slot="title">
                        <i :class="item.icon"></i>
                        <span v-if="!fold" slot="title" v-text="item.name"></span>
                    </template>
                        
                     <template v-for="(sub,j) in item.models">
                     
                    <el-menu-item-group  v-if="!sub.models" :title="sub.name" :key="sub.name">
                        <el-menu-item :index="sub.eid+''" @click="openTab(sub,item.eid)">
                            <i :class="sub.icon"></i>
                            <span slot="title" v-text="sub.name"></span>
                        </el-menu-item>
                    </el-menu-item-group>
                    
                    <el-submenu  v-else>
                       <template slot="title">
                            <i :class="sub.icon"></i>
                            <span v-if="!fold" slot="title" v-text="sub.name"></span>
                        </template>
                        <sub-menu :menus="sub.models" :fold="fold"></sub-menu>
                    </el-submenu>
                    </template>
                    
                </el-submenu>
    
            </template>
        </div>
    `

});
Vue.component('multiple-menu', {
    props: ['menus', 'openTab', 'menuActive', 'fold'],
    template: `
     <el-menu :unique-opened="true" :default-active="menuActive+''" :collapse="fold">
        <sub-menu :menus="menus" :fold="fold"></sub-menu>
    </el-menu>
    `
});