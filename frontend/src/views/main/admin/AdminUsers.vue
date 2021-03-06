<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Manage Users
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/users/create">Create User</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="users">
      <template slot="item" slot-scope="props">
        <tr>
          <td>{{ props.item.name }}</td>
          <td>{{ props.item.email }}</td>
          <td>{{ props.item.full_name }}</td>
          <td>
            <v-icon v-if="props.item.is_active">mdi-check</v-icon>
          </td>
          <td>
            <v-icon v-if="props.item.is_superuser">mdi-check</v-icon>
          </td>
          <td class="justify-center layout px-0">
            <v-tooltip top>
              <span>Edit</span>
              <template v-slot:activator="{ on }">
                <v-btn v-on="on" text :to="{name: 'main-admin-users-edit', params: {id: props.item.id}}">
                  <v-icon>mdi-square-edit-outline</v-icon>
                </v-btn>
              </template>
            </v-tooltip>
          </td>
        </tr>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import {Store} from 'vuex';
  import {IUserProfile} from '@/interfaces';
  import {readAdminUsers} from '@/store/admin/getters';
  import {dispatchGetUsers} from '@/store/admin/actions';

  @Component
  export default class AdminUsers extends Vue {
    public headers = [
      {
        text: 'Name',
        sortable: true,
        value: 'name',
        align: 'left',
      },
      {
        text: 'Email',
        sortable: true,
        value: 'email',
        align: 'left',
      },
      {
        text: 'Full Name',
        sortable: true,
        value: 'full_name',
        align: 'left',
      },
      {
        text: 'Is Active',
        sortable: true,
        value: 'isActive',
        align: 'left',
      },
      {
        text: 'Is Superuser',
        sortable: true,
        value: 'isSuperuser',
        align: 'left',
      },
      {
        text: 'Actions',
        value: 'id',
      },
    ];

    get users() {
      return readAdminUsers(this.$store);
    }

    public async mounted() {
      await dispatchGetUsers(this.$store);
    }
  }
</script>
