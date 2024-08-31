import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4.0 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Ashuthosh Shridhar ~",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "notes.ashuftw.com",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "created",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      /*
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },*/

      colors: {

lightMode: {
  light: "#faf7f4", // Very light beige, almost white (main background)
  lightgray: "#f0e6d9", // Light beige (subtle background variation)
  gray: "#8c7a6b", // Darker muted brown (softer text or elements)
  darkgray: "#5a4d40", // Darker brown (for stronger contrast elements)
  dark: "#0a0908", // Nearly black (main text color)
  secondary: "#3d3631", // Very dark brown (secondary text or elements)
  tertiary: "#cec3b5", // Light grayish brown (for additional contrast)
  highlight: "rgba(90, 77, 64, 0.15)", // Darker brown with reduced opacity
  textHighlight: "#0a090888", // Nearly black with reduced opacity
},
  darkMode: {
    light: "#0f0d0b",      // Theme (very dark brown)
    lightgray: "#2c2520",  // Light Grey (slightly lighter than theme)
    gray: "#5a4d40",       // Dark Grey (medium brown)
    darkgray: "#b3a396",   // Typewriter (muted light brown)
    dark: "#e0d6c9",       // Midnightblue (very light beige)
    secondary: "#8c7a6b",  // Highlight Grey (light brown)
    tertiary: "#f0e6d9",   // Text (light beige)
    highlight: "rgba(140, 122, 107, 0.15)", // Highlight Grey with reduced opacity
    textHighlight: "#0f0d0b88", // Theme color with reduced opacity
  },
},

      
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
