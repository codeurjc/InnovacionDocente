package es.codeurjc.test.exam.GestorMatricula;

public class GestorMatricula {

   private BaseDatosAlumnos alumnos;

   public GestorMatricula(BaseDatosAlumnos alumnos) {
      this.alumnos = alumnos;
   }

   public boolean posibleMatricula(long idAlumno) {
      double[] notas = this.alumnos.getNotas(idAlumno);
      double suma = 0;
      for (double nota : notas) {
         suma += nota;
      }
      return suma >= notas.length * 9.5;
   }

}
