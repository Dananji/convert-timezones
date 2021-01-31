<template>
  <div>
    <h2>Convert Timezones</h2>
    <select class="form-control" v-model="selected" @change="selectedTimezone()">
        <option disabled value="">Please select a Timezone</option>
        <option v-for="timezone in timezoneList" :value="timezone" :key="timezone.id">
            {{ timezone.name }}
        </option>
    </select>
    <p v-if="selected">Timezone: {{ selected.name }}</p>
    <p v-if="selected">Current time: {{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Timezone',
  data() {
    return {
      msg: '',
      timezoneList: [],
      selected: '',
    };
  },
  methods: {
    getTimezones() {
      const path = 'http://localhost:5000/timezones';
      axios.get(path)
        .then((res) => {
          this.timezoneList = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    selectedTimezone() {
      const path = 'http://localhost:5000/time';
      axios.get(path, { params: { timezone: this.selected.name } })
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getTimezones();
  },
};
</script>
