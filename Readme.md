# Spotify-to-Instagram Music Status Feature

This repository allows you to add a "MSN What I'm listening to" feature to your Instagram account using Spotify. The application takes what you're currently listening to on Spotify and updates it on your Instagram story. This is a basic Python script you can run on your local machine.

## Getting Started

### Prerequisites

You need to have Python 3.8+ installed on your computer.

For Windows, install Python using Chocolatey:

```sh

choco install python

```

For MacOS, install Python using Homebrew and Pyenv:

```

brew install pyenv
pyenv install 3.9.2 

```

### Installing Python Packages

The next step is to install the required Python packages by running the following command:

```sh

pip3 install -r requirements.txt

```

### Setting up the Spotify App

1. Go to the [Spotify Developer's Dashboard.](https://developers.spotify.com)
2. Log in with your Spotify account.
3. Create a new application.
4. Set a Redirect URL. This can be something simple like `http://localhost`.
5. Note down the `Client ID` and `Client Secret` that Spotify provides for your application.

### Configuring the Environment Variables

Copy the provided `.env.local` file to `.env`, and fill the variables with your Spotify and Instagram details:

```env

SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
SPOTIFY_REDIRECT_URI=http://localhost
INSTAGRAM_USERNAME=
INSTAGRAM_PASSWORD=

```

### Running the Application

Once all the setup is complete, you can run the application with the following command:

```sh

python3 main.py

```

Upon first run, the application will prompt you to paste the URL that is opened in your browser. This step is required to authorize your application's access to your Spotify account.

## Contributing

Contributions, issues, and feature requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is under the MIT license. See LICENSE for more details.

## Contact

If you have any questions or suggestions, feel free to open an issue or pull request.
