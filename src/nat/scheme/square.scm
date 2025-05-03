(define (zero) '())
(define (add1 prev) (cons prev '()))
(define (zero? target) (null? target))
(define (prev target) (car target))

(define (two) (add1 (add1 (zero))))

(define (add target addend)
  (if (zero? target)
    addend
    (add1 (add (prev target) addend))))

(define (mul target mulend)
  (if (zero? target)
    (zero)
    (add (mul (prev target) mulend) mulend)))

(define (square x) (mul x x))

(square (square (square (square (two)))))
