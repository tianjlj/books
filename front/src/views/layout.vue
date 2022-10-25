<template>
  <a-layout style="min-height: 100vh">
    <a-layout-sider v-model:collapsed="collapsed" collapsible class="sider-left">
      <div class="logo">
        <cloud-outlined v-if="collapsed" />
        <span v-else>demo system</span>
      </div>
      <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
        <a-sub-menu key="sub1">

          <template #title>
            <span >
              <user-outlined />
              <span>接口管理</span>
            </span>
          </template>

          <a-menu-item v-for="tp in type" :key="tp">
            <router-link to="/apis">{{ tp }}</router-link>
          </a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub2">
          <template #title>
            <span>
              <team-outlined />
              <span>用例管理</span>
            </span>
          </template>
          <a-menu-item key="6">Team 1</a-menu-item>
          <a-menu-item key="8">Team 2</a-menu-item>
        </a-sub-menu>
        <a-menu-item key="9">
          <file-outlined />
          <span>File</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>

    <a-layout class="sider-right" :style="right_margin">
      <a-layout-header style="background: #fff; padding: 0" class="header" />
      <a-layout-content style="margin: 0 16px" class="content">
        <a-breadcrumb style="margin: 16px 5px">
          <a-breadcrumb-item>User</a-breadcrumb-item>
          <a-breadcrumb-item>Bill</a-breadcrumb-item>
        </a-breadcrumb>
        <div :style="{ padding: '24px', background: '#fff', minHeight: '360px' }">
          Bill is a cat.<br />
          是否折叠？{{ collapsed }}<br />
          {{ right_margin }}
          <router-view />
        </div>
      </a-layout-content>
      <a-layout-footer style="text-align: center">
        Ant Design ©2018 Created by Ant UED
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script setup>
import {
  PieChartOutlined,
  DesktopOutlined,
  UserOutlined,
  TeamOutlined,
  FileOutlined,
  CloudOutlined,
} from "@ant-design/icons-vue";
import { ref, computed, onMounted } from "vue";
import { get_apis, get_type } from "../api/apis";

const collapsed = ref(false);
const selectedKeys = ref(["1"]);
const right_margin = computed(() => {
  return collapsed.value ? "margin-left:80px" : "margin-left:200px";
});

// let apis = await get_apis()
const type = ref();
const dosom = async () => {
  let res = await get_type();
  let { data } = res;
  let { content } = data;
  console.log(content);
  type.value = content;
};
onMounted(() => {
  dosom()
});
</script>

<style>
.logo {
  height: 32px;
  margin: 16px;
  background: rgba(255, 255, 255, 0.3);
  color: white;
  text-align: center;
  line-height: 32px;
  font-size: 18px;
  overflow: hidden;
}

.site-layout .site-layout-background {
  background: #fff;
}
[data-theme="dark"] .site-layout .site-layout-background {
  background: #141414;
}
.sider-left {
  overflow: auto;
  left: 0;
  top: 0;
  bottom: 0;
  height: 100vh;
  position: fixed;
}
.sider-right {
}
.header {
  /* position: fixed; */
}
.content {
  height: 2000px;
}
</style>
