package es.codeurjc.test.exam.GestorMatricula;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class GestorMatriculaTest {

    BaseDatosAlumnos bd;
    GestorMatricula gestor;

    @BeforeEach
    public void setUp(){
        bd = mock(BaseDatosAlumnos.class);
        gestor = new GestorMatricula(bd);
    }

    @Test
    @DisplayName("Cuando las notas de un alumno son todas 10, se concede la matricula")
    public void test01(){
        // GIVEN 
        double[] notas = {10.0, 10.0, 10.0};
        when(bd.getNotas(anyLong())).thenReturn(notas);
        long fakeID = 1;
        // WHEN
        boolean matriculaConcedida = gestor.posibleMatricula(fakeID);
        // THEN
        assertTrue(matriculaConcedida);
        verify(bd).getNotas(fakeID);
    }

    @Test
    @DisplayName("Cuando las notas de un alumno no son todas 10, no se concede la matricula")
    public void test02(){
        // GIVEN 
        double[] notas = {9.0, 5.0, 8.3};
        when(bd.getNotas(anyLong())).thenReturn(notas);
        long fakeID = 2;
        // WHEN
        boolean matriculaConcedida = gestor.posibleMatricula(fakeID);
        // THEN
        assertFalse(matriculaConcedida);
        verify(bd).getNotas(fakeID);
    }

}
