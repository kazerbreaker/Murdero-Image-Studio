# El Murdero Image Studio

A powerful AI image generation web application built with Streamlit that creates stunning visuals using Chutes AI models.

![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-000000?style=for-the-badge&logo=ai&logoColor=white)

## 🚀 Features

- **Multiple AI Models**: Choose from 5 different Chutes AI models
- **Free & Premium Options**: 
  - Free: Chroma, JuggernautXL, Neta Lumina
  - Rate-limited: Qwen Image, FLUX-1 Schnell
- **High-Quality Output**: 1024x1024 resolution images
- **Advanced Controls**: Adjust guidance scale and inference steps
- **Download Ready**: Direct download of generated images
- **Modern UI**: Clean, responsive interface with custom styling
- **Session Management**: Persistent settings across interactions

## 📋 Prerequisites

- Python 3.8+
- Chutes AI API key
- Internet connection

## ⚙️ Installation

1. **Clone or download this repository**
   ```bash
   git clone <your-repo-url>
   cd your-project-directory
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Create or edit the `.env` file in the root directory
   - Add your Chutes AI API key:
     ```
     CHUTES_API_TOKEN=your_actual_api_key_here
     ```

## 🔑 Obtaining API Key

1. Visit [Chutes AI](https://chutes.ai)
2. Sign up for an account
3. Navigate to API settings
4. Generate your API token
5. Replace `YOUR_API_KEY_HERE` in the `.env` file with your actual token

## 🎯 Usage

1. **Start the application**:
   ```bash
   streamlit run streamlit_app/streamlit_app.py
   ```

2. **Open your browser** to the provided local URL (typically `http://localhost:8501`)

3. **Generate images**:
   - Select your preferred AI model
   - Enter a detailed description of the image you want
   - Adjust advanced settings if desired
   - Click "Generate Image"
   - Download your creation when ready

## 🎨 Supported Models

| Model | Type | Cost | Best For |
|-------|------|------|----------|
| Chroma | Free | Unlimited | General purpose, high quality |
| JuggernautXL | Free | Unlimited | Detailed, realistic images |
| Neta Lumina | Free | Unlimited | Artistic, creative outputs |
| Qwen Image | Premium | Rate-limited | Advanced, specialized generations |
| FLUX-1 Schnell | Premium | Rate-limited | Quick, efficient generations |

## ⚡ Advanced Settings

- **Guidance Scale** (1.0-20.0): Controls how closely the AI follows your prompt
- **Inference Steps** (10-150): More steps = higher quality but slower generation

## 🏗️ Project Structure

```
.
├── streamlit_app/
│   └── streamlit_app.py      # Main application
├── .env                      # Environment variables
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore rules
```

## 🛠️ Development

### Running in Development Mode
```bash
streamlit run streamlit_app/streamlit_app.py
```

### Code Style
This project follows PEP 8 guidelines. Consider using:
- `black` for code formatting
- `flake8` for linting
- `isort` for import sorting

### Adding New Features
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**API Key Error**
- Ensure your `.env` file contains the correct API key
- Verify the key is active on Chutes AI

**Module Not Found**
- Run `pip install -r requirements.txt` to install all dependencies

**Image Generation Fails**
- Check your internet connection
- Verify the Chutes AI service status

**Slow Performance**
- Reduce inference steps for faster generation
- Use lighter models like Chroma or FLUX-1 Schnell

## 📞 Support

If you encounter any problems or have questions:

1. Check the [troubleshooting](#-troubleshooting) section
2. Review the [Chutes AI documentation](https://docs.chutes.ai)
3. Create an issue in this repository

## 🙏 Acknowledgments

- **Chutes AI** for providing the image generation API
- **Streamlit** for the excellent web framework
- **PIL/Pillow** for image handling capabilities

---

**Note**: This application is for personal and educational use. Please comply with Chutes AI's terms of service and usage policies.

**Created by El Murdero** • **Powered by Chutes AI**