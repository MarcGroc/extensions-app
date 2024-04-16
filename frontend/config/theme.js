// Colors
import colors from 'vuetify/lib/util/colors';

const palette = {
  violeta: {
    primary: colors.purple.base, // primary main
    primarylight: colors.purple.lighten4, // primary light
    primarydark: colors.purple.darken3, // primary dark
    secondary: colors.lightGreen.base, // secondary main
    secondarylight: colors.lightGreen.lighten4, // secondary light
    secondarydark: colors.lightGreen.darken3, // secondary dark
    anchor: colors.purple.base, // link
  },
};

const theme = {
  ...palette.violeta,
};

export default theme;
