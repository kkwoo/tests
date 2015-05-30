import unittest
from context import battleship

class TestBattleshipGame(unittest.TestCase):

  def setUp(self):
    self.a=battleship.game.main.BattleShipGame()

  def test_deploy_carrier(self):
    self.a.player1board.deploy_ship(battleship.game.ships.Carrier(battleship.game.coordinate.Coordinate(2,2)))
    self.assertEqual( len(self.a.player1board.armada), 1)

  def test_sink_carrier(self):
    self.test_deploy_carrier()
    self.a.player2_attacks_coordinate(battleship.game.coordinate.Coordinate(2,2))
    self.a.player2_attacks_coordinate(battleship.game.coordinate.Coordinate(2,3))
    self.a.player2_attacks_coordinate(battleship.game.coordinate.Coordinate(2,4))
    self.a.player2_attacks_coordinate(battleship.game.coordinate.Coordinate(2,5))
    self.a.player2_attacks_coordinate(battleship.game.coordinate.Coordinate(2,6))
    current_ship=self.a.player1board.armada.pop()
    self.assertEqual( current_ship.afloat(), False)

  def test_arrange_player1board(self):
    self.a.player1board.deploy_ship(battleship.game.ships.Carrier(battleship.game.coordinate.Coordinate(2,2)))
    self.a.player1board.deploy_ship(battleship.game.ships.Battleship(battleship.game.coordinate.Coordinate(4,4)))
    self.a.player1board.deploy_ship(battleship.game.ships.Submarine(battleship.game.coordinate.Coordinate(6,6)))
    self.a.player1board.deploy_ship(battleship.game.ships.Cruiser(battleship.game.coordinate.Coordinate(7,7)))
    self.a.player1board.deploy_ship(battleship.game.ships.Patrol(battleship.game.coordinate.Coordinate(8,8)))
    self.assertEqual( len(self.a.player1board.armada), 5)

  def test_arrange_player2board(self):
    self.a.player2board.deploy_ship(battleship.game.ships.Carrier(battleship.game.coordinate.Coordinate(1,3)))
    self.a.player2board.deploy_ship(battleship.game.ships.Battleship(battleship.game.coordinate.Coordinate(3,3)))
    self.a.player2board.deploy_ship(battleship.game.ships.Submarine(battleship.game.coordinate.Coordinate(5,3)))
    self.a.player2board.deploy_ship(battleship.game.ships.Cruiser(battleship.game.coordinate.Coordinate(7,3)))
    self.a.player2board.deploy_ship(battleship.game.ships.Patrol(battleship.game.coordinate.Coordinate(9,3)))
    self.assertEqual( len(self.a.player2board.armada), 5)

  def test_players_moves(self):
    self.test_arrange_player1board()
    self.test_arrange_player2board()
    self.a.player1_attacks_coordinate(battleship.game.coordinate.Coordinate(3,3))
    self.assertEqual( self.a.player2board.latest_received_attack_successful(), True)
    
    self.a.player2_attacks_coordinate(battleship.game.coordinate.Coordinate(9,3))
    self.assertEqual( self.a.player1board.latest_received_attack_successful(), False)
    
    self.a.player1_attacks_coordinate(battleship.game.coordinate.Coordinate(9,3))
    self.assertEqual( self.a.player2board.latest_received_attack_successful(), True)
    self.assertEqual( len([ship for ship in list(self.a.player2board.armada) if len(ship.coordinates) == 0]), 1)
if __name__ == '__main__':
    unittest.main()