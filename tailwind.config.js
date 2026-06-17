/** @type {import('tailwindcss').Config} */
module.exports = {
  // Escanea las plantillas (incluye el HTML generado en dist por si acaso).
  content: ["./templates/**/*.html", "./dist/**/*.html"],
  theme: {
    extend: {
      colors: {
        // Identidad corporativa CGN (Manual de Identidad Visual v10)
        cgn: {
          verde: "#29977C",
          verdeos: "#176551", // verde oscuro: texto sobre claro (≥4.5:1) y fondos
          gris: "#9B9A98",
          naranja: "#DA9440",
          naranjaos: "#9A5E15", // naranja oscuro: texto/insignias sobre claro (≥4.5:1)
          negro: "#1F140F",
          grisos: "#616160",
        },
        hacienda: "#B38B40", // color identificador sector Hacienda
        // Paleta GOV.CO (Kit UI 9.2)
        govco: {
          cobalt: "#0943B5",
          havelock: "#3366CC",
          solitude: "#E6EFFA",
          corn: "#FFF8E1",
          smoke: "#F4F4F4",
          silver: "#C2C2C2",
        },
        estado: {
          error: "#A80521",
          alerta: "#F3B228",
          exito: "#069169",
        },
      },
      fontFamily: {
        titulo: ['"Nunito Sans"', "system-ui", "sans-serif"],
        cuerpo: ["Verdana", "Geneva", "system-ui", "sans-serif"],
      },
      maxWidth: { contenido: "1320px" },
    },
  },
  plugins: [],
};
