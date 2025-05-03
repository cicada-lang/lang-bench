(defun zero () '())
(defun add1 (prev) (cons prev '()))
(defun zero? (target) (eq target '()))
(defun prev (target) (car target))

(defun two () (add1 (add1 (zero))))

(defun add (target addend)
  (if (zero? target)
    addend
    (add1 (add (prev target) addend))))

(defun mul (target mulend)
  (if (zero? target)
    (zero)
    (add (mul (prev target) mulend) mulend)))

(defun square (x) (mul x x))

(square (square (square (square (two)))))

(quit)
