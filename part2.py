import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


class PlaylistDB:
    def __init__(self):
        self.con = None

    def connect(self):
        try:
            self.con = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME')
            )
            print("Connection successful")
        except Exception as err:
            print("Connection error:", err)

    # ---------------- PLAYLIST ---------------- #

    def add_playlist(self):
        try:
            name = input("Playlist Name: ")
            desc = input("Description: ")

            cursor = self.con.cursor()
            sql = "INSERT INTO playlists (name, description) VALUES (%s, %s)"
            cursor.execute(sql, (name, desc))
            self.con.commit()

            print("Playlist added")
            cursor.close()

        except Exception as err:
            print(err)

    def view_playlists(self):
        try:
            cursor = self.con.cursor()
            cursor.execute("SELECT * FROM playlists")

            for row in cursor:
                print(f"ID: {row[0]} | Name: {row[1]} | Desc: {row[2]}")

            cursor.close()

        except Exception as err:
            print(err)

    def edit_playlist(self):
        try:
            pid = input("Playlist ID: ")
            name = input("New Name: ")
            desc = input("New Description: ")

            cursor = self.con.cursor()
            sql = "UPDATE playlists SET name=%s, description=%s WHERE playlist_id=%s"
            cursor.execute(sql, (name, desc, pid))
            self.con.commit()

            print("Playlist updated")
            cursor.close()

        except Exception as err:
            print(err)

    def delete_playlist(self):
        try:
            pid = input("Playlist ID: ")

            cursor = self.con.cursor()
            cursor.execute("DELETE FROM playlists WHERE playlist_id=%s", (pid,))
            self.con.commit()

            print("Playlist deleted")
            cursor.close()

        except Exception as err:
            print(err)

    # ---------------- SONGS ---------------- #

    def add_song(self):
        try:
            title = input("Title: ")
            channel = input("Artist/Channel: ")
            original = input("Is Original (y/n): ").lower() == 'y'
            duration = float(input("Duration: "))
            playlist_id = input("Playlist ID: ")

            cursor = self.con.cursor()
            sql = """
            INSERT INTO songs (title, channel, is_original, duration, playlist_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (title, channel, original, duration, playlist_id))
            self.con.commit()

            print("Song added")
            cursor.close()

        except Exception as err:
            print(err)

    def view_songs(self):
        try:
            cursor = self.con.cursor()

            query = """
            SELECT s.song_id, s.title, s.channel, s.is_original, s.duration, p.name
            FROM songs s
            JOIN playlists p ON s.playlist_id = p.playlist_id
            """

            cursor.execute(query)

            for row in cursor:
                print(f"""
ID: {row[0]}
Title: {row[1]}
Artist: {row[2]}
Original: {row[3]}
Duration: {row[4]}
Playlist: {row[5]}
-----------------------
""")

            cursor.close()

        except Exception as err:
            print(err)

    def edit_song(self):
        try:
            sid = input("Song ID: ")
            title = input("Title: ")
            channel = input("Artist: ")
            original = input("Original (y/n): ").lower() == 'y'
            duration = float(input("Duration: "))

            cursor = self.con.cursor()
            sql = """
            UPDATE songs 
            SET title=%s, channel=%s, is_original=%s, duration=%s 
            WHERE song_id=%s
            """
            cursor.execute(sql, (title, channel, original, duration, sid))
            self.con.commit()

            print("Song updated")
            cursor.close()

        except Exception as err:
            print(err)

    def delete_song(self):
        try:
            sid = input("Song ID: ")

            cursor = self.con.cursor()
            cursor.execute("DELETE FROM songs WHERE song_id=%s", (sid,))
            self.con.commit()

            print("Song deleted")
            cursor.close()

        except Exception as err:
            print(err)

    def search_song(self):
        try:
            sid = input("Song ID: ")

            cursor = self.con.cursor()
            cursor.execute("SELECT * FROM songs WHERE song_id=%s", (sid,))
            row = cursor.fetchone()

            if row:
                print(row)
            else:
                print("Not found")

            cursor.close()

        except Exception as err:
            print(err)

    def view_songs_by_playlist(self):
        try:
            cursor = self.con.cursor()

            cursor.execute("SELECT playlist_id, name FROM playlists")
            print("Playlists:")
            for row in cursor:
                print(f"{row[0]} - {row[1]}")

            pid = input("Enter Playlist ID: ")

            query = """
            SELECT title, channel, is_original, duration
            FROM songs
            WHERE playlist_id=%s
            """
            cursor.execute(query, (pid,))
            results = cursor.fetchall()

            if results:
                for row in results:
                    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
            else:
                print("No songs found")

            cursor.close()

        except Exception as err:
            print(err)

    # ---------------- MENU ---------------- #

    def menu(self):
        while True:
            print("""
1. Add Playlist
2. View Playlists
3. Edit Playlist
4. Delete Playlist
5. Add Song
6. View Songs
7. Edit Song
8. Delete Song
9. Search Song
10. View Songs by Playlist
11. Exit
""")

            choice = input("Choice: ")

            if choice == "1":
                self.connect()
                self.add_playlist()

            elif choice == "2":
                self.connect()
                self.view_playlists()

            elif choice == "3":
                self.connect()
                self.edit_playlist()

            elif choice == "4":
                self.connect()
                self.delete_playlist()

            elif choice == "5":
                self.connect()
                self.add_song()

            elif choice == "6":
                self.connect()
                self.view_songs()

            elif choice == "7":
                self.connect()
                self.edit_song()

            elif choice == "8":
                self.connect()
                self.delete_song()

            elif choice == "9":
                self.connect()
                self.search_song()

            elif choice == "10":
                self.connect()
                self.view_songs_by_playlist()

            elif choice == "11":
                print("Goodbye")
                break


if __name__ == "__main__":
    db = PlaylistDB()
    db.menu()