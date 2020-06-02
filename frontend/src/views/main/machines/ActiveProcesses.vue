<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Active Processes of machine {{this.machine.name}}
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-data-table :headers="headers" :items="processes">
      <template slot="item" slot-scope="props">
        <tr>
          <td>{{ props.item.name }}</td>
          <td>{{ props.item.host }}</td>
        </tr>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import {readOneMachine} from '@/store/machines/getters';
  import {dispatchGetMachine} from '@/store/machines/actions';

  @Component
  export default class MachinesActiveProcesses extends Vue {
    public headers = [
      {
        text: 'Name',
        sortable: true,
        value: 'name',
        align: 'left',
      },
      {
        text: 'Hash',
        value: 'hash',
        align: 'left',
      },
    ];
    get machine() {
      return readOneMachine(this.$store)(+this.$router.currentRoute.params.id);
    }
    public async mounted() {
      await dispatchGetMachine(this.$store, {id: +this.$router.currentRoute.params.id});
    }
  }
</script>