import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { MachinesState } from './state';

const defaultState: MachinesState = {
  machines: [],
};

export const machinesModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
