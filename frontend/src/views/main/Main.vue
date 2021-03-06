<template>
  <div>
    <v-navigation-drawer  :mini-variant="miniDrawer" v-model="showDrawer" fixed app>
        <v-list nav>
          <v-subheader v-show="!miniDrawer">Main menu</v-subheader>
          <v-list-item to="/main/dashboard">
            <v-list-item-action>
              <v-icon>mdi-web</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Dashboard</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item to="/main/profile/view">
            <v-list-item-action>
              <v-icon>mdi-account-circle</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Profile</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item to="/main/profile/edit">
            <v-list-item-action>
              <v-icon>mdi-account-edit</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Edit Profile</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item to="/main/profile/password">
            <v-list-item-action>
              <v-icon>mdi-onepassword</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Change Password</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

        </v-list>

        <v-divider></v-divider>

        <v-list nav>
          <v-subheader v-show="!miniDrawer">Machines</v-subheader>
          <v-list-item to="/main/machines">
            <v-list-item-action>
              <v-icon>mdi-cellphone-link</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Machines Dashboard</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list nav v-show="hasAdminAccess">
          <v-subheader v-show="!miniDrawer">Admin</v-subheader>
          <v-list-item to="/main/admin/users/all">
            <v-list-item-action>
              <v-icon>mdi-account-group</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Manage Users</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item to="/main/admin/users/create">
            <v-list-item-action>
              <v-icon>mdi-account-plus</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Create User</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>

        <v-spacer></v-spacer>
        <v-list nav>
          <v-list-item @click="logout">
            <v-list-item-action>
              <v-icon>mdi-logout</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item @click="switchMiniDrawer">
            <v-list-item-action>
              <v-icon v-html="miniDrawer ? 'mdi-dots-vertical' : 'mdi-dots-vertical'"></v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Collapse</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
    </v-navigation-drawer>

    <v-app-bar color="primary" app>
      <v-app-bar-nav-icon @click.stop="switchShowDrawer"></v-app-bar-nav-icon>
      <v-toolbar-title v-text="appName"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu bottom left offset-y>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" icon>
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item to="/main/profile">
            <v-list-item-content>
              <v-list-item-title>Profile</v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>mdi-account-circle</v-icon>
            </v-list-item-action>
          </v-list-item>
          <v-list-item @click="logout">
            <v-list-item-content>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>mdi-logout</v-icon>
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-content>
      <router-view></router-view>
    </v-content>
    <v-footer class="pa-3" fixed app>
      <v-spacer></v-spacer>
      <span>&copy; {{appName}}</span>
    </v-footer>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';

  import {appName} from '@/env';
  import {readDashboardMiniDrawer, readDashboardShowDrawer, readHasAdminAccess} from '@/store/main/getters';
  import {commitSetDashboardMiniDrawer, commitSetDashboardShowDrawer} from '@/store/main/mutations';
  import {dispatchUserLogOut} from '@/store/main/actions';

  const routeGuardMain = async (to, from, next) => {
    if (to.path === '/main') {
      next('/main/dashboard');
    } else {
      next();
    }
  };

  @Component
  export default class Main extends Vue {
    public appName = appName;

    public beforeRouteEnter(to, from, next) {
      routeGuardMain(to, from, next);
    }

    public beforeRouteUpdate(to, from, next) {
      routeGuardMain(to, from, next);
    }

    get miniDrawer() {
      return readDashboardMiniDrawer(this.$store);
    }

    get showDrawer() {
      return readDashboardShowDrawer(this.$store);
    }

    set showDrawer(value) {
      commitSetDashboardShowDrawer(this.$store, value);
    }

    public switchShowDrawer() {
      commitSetDashboardShowDrawer(
        this.$store,
        !readDashboardShowDrawer(this.$store),
      );
    }

    public switchMiniDrawer() {
      commitSetDashboardMiniDrawer(
        this.$store,
        !readDashboardMiniDrawer(this.$store),
      );
    }

    public get hasAdminAccess() {
      return readHasAdminAccess(this.$store);
    }

    public async logout() {
      await dispatchUserLogOut(this.$store);
    }
  }
</script>
