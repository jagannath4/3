class WaterJugState:
    def_init_(self,jug1,jug2):
      self.jug1=jug1
      self.jug2=jug2
    def_eq_(self,other):
    return self.jug1==other.jug1 and jug2==other.jug2
    def_hash_(self):
    return hash((self.jug1,self.jug2))
    def dfs(current_state, visited,jug1_capacity,jug2_capacity,target_volumne):
        if current_state.jug1==target_volume or current state_.jug2_capacity,target_volume):
            if current_state.jug1==target_volumne:
        print("jug 1 now has",target_volumne,"litres")
        else:
