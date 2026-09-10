/**
 * Renderiza un árbol binario usando D3.js
 * @param {Object} arbolData - Estructura {valor, izquierdo, derecho}
 * @param {string} containerSelector - Selector CSS del contenedor
 * @param {boolean} esExpresion - true si es árbol de expresión (colorea operadores)
 */
function dibujarArbolD3(arbolData, containerSelector, esExpresion = false) {
    const container = d3.select(containerSelector);
    container.html('');

    // Si no hay árbol, mostrar mensaje
    if (!arbolData) {
        container.append('p')
            .attr('class', 'placeholder-text')
            .style('text-align', 'center')
            .style('padding', '50px')
            .style('color', '#999')
            .text('El árbol está vacío');
        return;
    }

    // ===== Configuración =====
    const width = 1000;
    const height = 500;
    const nodeRadius = 24;
    const margin = 60;

    // ===== Crear SVG =====
    const svg = container.append('svg')
        .attr('width', '100%')
        .attr('height', height)
        .attr('viewBox', [0, 0, width, height])
        .style('background', '#fafafa')
        .style('border-radius', '8px');

    // Grupo principal (para zoom/pan)
    const g = svg.append('g');

    // Zoom y pan con la rueda del mouse
    svg.call(d3.zoom()
        .scaleExtent([0.3, 3])
        .on('zoom', (event) => {
            g.attr('transform', event.transform);
        })
    );

    // ===== Convertir a jerarquía D3 =====
    // D3 espera una lista de hijos; el backend manda izquierdo/derecho por separado.
    const root = d3.hierarchy(arbolData, d => {
        const children = [];
        if (d.izquierdo) children.push(d.izquierdo);
        if (d.derecho) children.push(d.derecho);
        return children.length ? children : null;
    });

    // ===== Calcular layout del árbol =====
    d3.tree()
        .size([width - margin * 2, height - margin * 2])
        .separation((a, b) => (a.parent === b.parent ? 1 : 1.5))(root);

    // Centrar el árbol
    g.attr('transform', `translate(${margin}, ${margin})`);

    // ===== Dibujar enlaces (líneas) =====
    g.selectAll('.link')
        .data(root.links())
        .enter()
        .append('path')
        .attr('class', 'link')
        .attr('fill', 'none')
        .attr('stroke', '#bbb')
        .attr('stroke-width', 2)
        .attr('d', d3.linkVertical()
            .x(d => d.x)
            .y(d => d.y)
        );

    // ===== Dibujar nodos =====
    const nodes = g.selectAll('.node')
        .data(root.descendants())
        .enter()
        .append('g')
        .attr('class', 'node')
        .attr('transform', d => `translate(${d.x}, ${d.y})`);

    // Círculo del nodo
    nodes.append('circle')
        .attr('r', nodeRadius)
        .attr('fill', d => obtenerColorNodo(d.data.valor, esExpresion))
        .attr('stroke', '#fff')
        .attr('stroke-width', 3)
        .style('cursor', 'pointer')
        .style('filter', 'drop-shadow(0 2px 4px rgba(0,0,0,0.2))')
        .on('mouseover', function () {
            d3.select(this).transition().duration(200).attr('r', nodeRadius + 4);
        })
        .on('mouseout', function () {
            d3.select(this).transition().duration(200).attr('r', nodeRadius);
        });

    // Texto del nodo
    nodes.append('text')
        .attr('dy', '0.35em')
        .attr('text-anchor', 'middle')
        .attr('fill', 'white')
        .attr('font-weight', 'bold')
        .attr('font-size', d => String(d.data.valor).length > 3 ? '11px' : '14px')
        .style('pointer-events', 'none')
        .text(d => d.data.valor);
}

/**
 * Devuelve el color según el tipo de nodo
 */
function obtenerColorNodo(valor, esExpresion) {
    if (esExpresion) {
        const operadores = ['+', '-', '*', '/', '^'];
        return operadores.includes(valor) ? '#FF9800' : '#2196F3';
    }
    return '#4CAF50';
}