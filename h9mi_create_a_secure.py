import hashlib
import os
import time
from cryptography.fernet import Fernet

class GamePrototypeIntegrator:
    def __init__(self):
        self.games = {}
        self.keys = {}

    def add_game(self, game_id, game_data):
        self.games[game_id] = game_data
        self.keys[game_id] = self.generate_key()

    def generate_key(self):
        key = Fernet.generate_key()
        return key

    def encrypt_game_data(self, game_id):
        key = self.keys[game_id]
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(self.games[game_id].encode())
        return encrypted_data

    def decrypt_game_data(self, game_id, encrypted_data):
        key = self.keys[game_id]
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
        return decrypted_data

    def verify_gameegrity(self, game_id, encrypted_data):
        expected_hash = self.games[game_id]
        actual_hash = hashlib.sha256(encrypted_data).hexdigest()
        return expected_hash == actual_hash

    def integrate_game(self, game_id):
        encrypted_data = self.encrypt_game_data(game_id)
        if self.verify_gameegrity(game_id, encrypted_data):
            print("Game integrated successfully!")
            return encrypted_data
        else:
            print("Game integrity verification failed!")

# Example usage:
if __name__ == "__main__":
    integrator = GamePrototypeIntegrator()
    game_id = "my_game"
    game_data = "This is a sample game data"
    integrator.add_game(game_id, game_data)
    encrypted_data = integrator.integrate_game(game_id)
    print("Encrypted game data:", encrypted_data)