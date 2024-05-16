function load_canvas() {

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById("figure").appendChild(renderer.domElement);

    // Oświetlenie 
    var light;
    light = new THREE.DirectionalLight();
    light.position.set(-10, -20, 1);
    camera.add(light);
    scene.add(camera);

    const material = new THREE.MeshPhongMaterial({ color: 0xffffff });

    camera.position.z = 100;
    camera.position.y = -10;

    // głowa

    const geometry = new THREE.SphereGeometry(15, 32, 16);
    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);

    // Szyja
    const szyja_geometry_1 = new THREE.CylinderGeometry(13, 13, 3, 32);
    const szyja_1 = new THREE.Mesh(szyja_geometry_1, material);
    szyja_1.position.set(0, -10, 0);
    scene.add(szyja_1);

    const szyja_geometry_2 = new THREE.CylinderGeometry(12, 12, 6, 32);
    const szyja_2 = new THREE.Mesh(szyja_geometry_2, material);
    szyja_2.position.set(0, -13, 0);
    scene.add(szyja_2);

    // ciało

    const points = [];
    for (let i = 0; i < 10; i++) {
        points.push(new THREE.Vector2((Math.cos(i * 0.2) * 3 + 6), (i - 5) * 4));
    }
    const cialo_geometry = new THREE.LatheGeometry(points);
    const cialo = new THREE.Mesh(cialo_geometry, material);
    cialo.position.set(0, -25, 0);
    scene.add(cialo);

    // podstawa

    const podstawa_geometry_1 = new THREE.CylinderGeometry(10, 14, 5, 32);
    const podstawa_1 = new THREE.Mesh(podstawa_geometry_1, material);
    podstawa_1.position.set(0, -45, 0);
    scene.add(podstawa_1);

    const podstawa_geometry_2 = new THREE.CylinderGeometry(15, 15, 2, 32);
    const podstawa_2 = new THREE.Mesh(podstawa_geometry_2, material);
    podstawa_2.position.set(0, -48, 0);
    scene.add(podstawa_2);

    const podstawa_geometry_3 = new THREE.CylinderGeometry(17, 17, 2, 32);
    const podstawa_3 = new THREE.Mesh(podstawa_geometry_3, material);
    podstawa_3.position.set(0, -50, 0);
    scene.add(podstawa_3);

    const podstawa_geometry_4 = new THREE.CylinderGeometry(19, 19, 2, 32);
    const podstawa_4 = new THREE.Mesh(podstawa_geometry_4, material);
    podstawa_4.position.set(0, -52, 0);
    scene.add(podstawa_4);

    function animate() {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
    }
    animate();

}

load_canvas();
