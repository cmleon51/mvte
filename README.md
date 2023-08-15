# MVTE
Move files on your unix system automatically using 'glob' as a matching function

## Configuration
Everything is configured in the file *'~/.config/mvte/mvte.yml'* (automatically created if it doesn't exist).
The file should be structured as follows:
```yaml
identifier:
  pattern: "your glob pattern" 
  src: "where to find the files"
  destination: "where to move the files"
```
You can define as many identifiers as you want.

### Examples
```yaml
Mp3_4_files:
  src: "~/Downloads"
  pattern: "*.mp[34]"
  destination: "~/Videos/YoutubeVideos"
```
```yaml
Telegram:
  pattern: "Name*"
  src: "~/Downloads/Telegram Desktop"
  destination: "~/Documents/Shows/Invincible"
```
