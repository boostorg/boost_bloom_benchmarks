# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.55</td>
    <td align="right">5.39</td>
    <td align="right">4.25</td>
    <td align="right">12.41</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">0.97</td>
    <td align="right">1.07</td>
    <td align="right">1.62</td>
    <td align="right">1.49</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.12</td>
    <td align="right">1.24</td>
    <td align="right">1.25</td>
    <td align="right">1.24</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.25</td>
    <td align="right">1.24</td>
    <td align="right">1.23</td>
    <td align="right">1.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">0.96</td>
    <td align="right">1.11</td>
    <td align="right">1.17</td>
    <td align="right">1.28</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.15</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="right">1.29</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.25</td>
    <td align="right">1.24</td>
    <td align="right">1.26</td>
    <td align="right">1.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">0.94</td>
    <td align="right">1.11</td>
    <td align="right">0.93</td>
    <td align="right">1.20</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.19</td>
    <td align="right">1.32</td>
    <td align="right">1.31</td>
    <td align="right">1.33</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.28</td>
    <td align="right">1.26</td>
    <td align="right">1.16</td>
    <td align="right">1.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">0.89</td>
    <td align="right">1.15</td>
    <td align="right">0.77</td>
    <td align="right">1.16</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.20</td>
    <td align="right">1.30</td>
    <td align="right">1.29</td>
    <td align="right">1.19</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.28</td>
    <td align="right">1.13</td>
    <td align="right">1.14</td>
    <td align="right">1.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.25</td>
    <td align="right">1.29</td>
    <td align="right">1.28</td>
    <td align="right">1.27</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.17</td>
    <td align="right">1.46</td>
    <td align="right">1.47</td>
    <td align="right">1.46</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.04</td>
    <td align="right">0.91</td>
    <td align="right">0.89</td>
    <td align="right">0.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">0.99</td>
    <td align="right">1.76</td>
    <td align="right">1.64</td>
    <td align="right">1.67</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">1.05</td>
    <td align="right">1.70</td>
    <td align="right">1.71</td>
    <td align="right">1.67</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.12</td>
    <td align="right">0.94</td>
    <td align="right">0.95</td>
    <td align="right">0.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">1.22</td>
    <td align="right">1.61</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">0.94</td>
    <td align="right">1.55</td>
    <td align="right">1.56</td>
    <td align="right">1.56</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">1.00</td>
    <td align="right">1.09</td>
    <td align="right">1.00</td>
    <td align="right">1.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">1.17</td>
    <td align="right">1.22</td>
    <td align="right">1.23</td>
    <td align="right">1.21</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">1.10</td>
    <td align="right">1.51</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">1.00</td>
    <td align="right">1.09</td>
    <td align="right">0.97</td>
    <td align="right">1.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">1.01</td>
    <td align="right">0.90</td>
    <td align="right">0.89</td>
    <td align="right">0.87</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">0.96</td>
    <td align="right">0.98</td>
    <td align="right">0.97</td>
    <td align="right">0.94</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">0.89</td>
    <td align="right">0.99</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.04</td>
    <td align="right">0.89</td>
    <td align="right">0.89</td>
    <td align="right">0.90</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">0.85</td>
    <td align="right">0.91</td>
    <td align="right">0.90</td>
    <td align="right">0.91</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">0.94</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">0.90</td>
    <td align="right">1.08</td>
    <td align="right">0.99</td>
    <td align="right">1.07</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">0.96</td>
    <td align="right">1.08</td>
    <td align="right">1.07</td>
    <td align="right">1.05</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">0.95</td>
    <td align="right">1.08</td>
    <td align="right">1.09</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">0.91</td>
    <td align="right">1.08</td>
    <td align="right">0.98</td>
    <td align="right">1.07</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">1.11</td>
    <td align="right">1.07</td>
    <td align="right">1.08</td>
    <td align="right">1.04</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">1.08</td>
    <td align="right">1.07</td>
    <td align="right">1.08</td>
    <td align="right">1.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">1.26</td>
    <td align="right">1.43</td>
    <td align="right">1.18</td>
    <td align="right">1.33</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">0.97</td>
    <td align="right">1.52</td>
    <td align="right">1.18</td>
    <td align="right">1.29</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">0.97</td>
    <td align="right">1.08</td>
    <td align="right">1.08</td>
    <td align="right">1.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">1.28</td>
    <td align="right">1.46</td>
    <td align="right">1.12</td>
    <td align="right">1.41</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">0.95</td>
    <td align="right">1.45</td>
    <td align="right">1.18</td>
    <td align="right">1.33</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">0.91</td>
    <td align="right">0.95</td>
    <td align="right">0.93</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">1.35</td>
    <td align="right">1.24</td>
    <td align="right">1.10</td>
    <td align="right">1.37</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">1.04</td>
    <td align="right">1.39</td>
    <td align="right">1.20</td>
    <td align="right">1.38</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">0.91</td>
    <td align="right">0.97</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">1.26</td>
    <td align="right">1.37</td>
    <td align="right">1.16</td>
    <td align="right">1.49</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">1.12</td>
    <td align="right">1.44</td>
    <td align="right">1.20</td>
    <td align="right">1.35</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">0.88</td>
    <td align="right">0.92</td>
    <td align="right">0.93</td>
    <td align="right">0.93</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.10</td>
    <td align="right">23.12</td>
    <td align="right">14.43</td>
    <td align="right">30.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">1.01</td>
    <td align="right">1.14</td>
    <td align="right">1.44</td>
    <td align="right">1.37</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.18</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.31</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">1.32</td>
    <td align="right">1.33</td>
    <td align="right">0.71</td>
    <td align="right">1.05</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">1.20</td>
    <td align="right">1.39</td>
    <td align="right">1.38</td>
    <td align="right">1.39</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">1.26</td>
    <td align="right">1.48</td>
    <td align="right">1.49</td>
    <td align="right">1.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">1.47</td>
    <td align="right">1.56</td>
    <td align="right">0.56</td>
    <td align="right">1.10</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">1.61</td>
    <td align="right">1.76</td>
    <td align="right">1.75</td>
    <td align="right">1.76</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">1.66</td>
    <td align="right">1.70</td>
    <td align="right">1.58</td>
    <td align="right">1.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">1.50</td>
    <td align="right">1.65</td>
    <td align="right">0.49</td>
    <td align="right">1.13</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">1.89</td>
    <td align="right">1.90</td>
    <td align="right">1.89</td>
    <td align="right">1.83</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">1.80</td>
    <td align="right">1.97</td>
    <td align="right">1.96</td>
    <td align="right">2.01</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">1.21</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">1.32</td>
    <td align="right">1.59</td>
    <td align="right">1.63</td>
    <td align="right">1.58</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">1.21</td>
    <td align="right">1.10</td>
    <td align="right">1.09</td>
    <td align="right">1.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">1.41</td>
    <td align="right">1.73</td>
    <td align="right">1.67</td>
    <td align="right">1.68</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">1.40</td>
    <td align="right">1.82</td>
    <td align="right">1.81</td>
    <td align="right">1.79</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">1.20</td>
    <td align="right">1.05</td>
    <td align="right">1.05</td>
    <td align="right">1.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">1.76</td>
    <td align="right">1.75</td>
    <td align="right">1.75</td>
    <td align="right">1.79</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">1.36</td>
    <td align="right">1.87</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">1.47</td>
    <td align="right">1.67</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">1.64</td>
    <td align="right">1.59</td>
    <td align="right">1.61</td>
    <td align="right">1.60</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">1.57</td>
    <td align="right">2.01</td>
    <td align="right">2.01</td>
    <td align="right">2.04</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">1.39</td>
    <td align="right">1.68</td>
    <td align="right">1.37</td>
    <td align="right">1.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">1.02</td>
    <td align="right">0.93</td>
    <td align="right">0.93</td>
    <td align="right">0.91</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">1.05</td>
    <td align="right">1.09</td>
    <td align="right">1.09</td>
    <td align="right">1.09</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">0.98</td>
    <td align="right">1.08</td>
    <td align="right">1.07</td>
    <td align="right">1.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">1.33</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="right">1.18</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">1.39</td>
    <td align="right">1.36</td>
    <td align="right">1.35</td>
    <td align="right">1.36</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">1.10</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
    <td align="right">1.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">1.41</td>
    <td align="right">1.65</td>
    <td align="right">1.37</td>
    <td align="right">1.35</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">1.45</td>
    <td align="right">1.55</td>
    <td align="right">1.43</td>
    <td align="right">1.37</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">1.37</td>
    <td align="right">1.60</td>
    <td align="right">1.54</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">1.37</td>
    <td align="right">1.68</td>
    <td align="right">1.38</td>
    <td align="right">1.39</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">1.59</td>
    <td align="right">1.62</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">1.47</td>
    <td align="right">1.70</td>
    <td align="right">1.52</td>
    <td align="right">1.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">1.42</td>
    <td align="right">1.54</td>
    <td align="right">1.26</td>
    <td align="right">1.49</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">0.99</td>
    <td align="right">1.42</td>
    <td align="right">1.31</td>
    <td align="right">1.40</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">0.91</td>
    <td align="right">0.86</td>
    <td align="right">0.87</td>
    <td align="right">0.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">1.71</td>
    <td align="right">1.77</td>
    <td align="right">1.29</td>
    <td align="right">1.70</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">1.40</td>
    <td align="right">1.84</td>
    <td align="right">1.40</td>
    <td align="right">1.63</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">1.30</td>
    <td align="right">1.31</td>
    <td align="right">1.32</td>
    <td align="right">1.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">2.11</td>
    <td align="right">2.11</td>
    <td align="right">1.24</td>
    <td align="right">1.90</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">1.75</td>
    <td align="right">2.05</td>
    <td align="right">1.46</td>
    <td align="right">1.86</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">1.17</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">2.64</td>
    <td align="right">2.76</td>
    <td align="right">1.40</td>
    <td align="right">2.41</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">2.18</td>
    <td align="right">2.43</td>
    <td align="right">1.45</td>
    <td align="right">2.13</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">1.03</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.30</td>
    <td align="right">5.95</td>
    <td align="right">4.29</td>
    <td align="right">12.89</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">0.85</td>
    <td align="right">0.83</td>
    <td align="right">1.36</td>
    <td align="right">1.19</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.06</td>
    <td align="right">1.75</td>
    <td align="right">1.76</td>
    <td align="right">1.73</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.01</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">0.86</td>
    <td align="right">0.83</td>
    <td align="right">0.95</td>
    <td align="right">1.01</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.09</td>
    <td align="right">1.92</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.03</td>
    <td align="right">1.63</td>
    <td align="right">1.90</td>
    <td align="right">1.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">0.84</td>
    <td align="right">0.83</td>
    <td align="right">0.76</td>
    <td align="right">0.94</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.08</td>
    <td align="right">2.01</td>
    <td align="right">2.01</td>
    <td align="right">2.03</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.02</td>
    <td align="right">1.98</td>
    <td align="right">1.98</td>
    <td align="right">1.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">0.80</td>
    <td align="right">0.80</td>
    <td align="right">0.61</td>
    <td align="right">0.82</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.08</td>
    <td align="right">2.06</td>
    <td align="right">2.06</td>
    <td align="right">2.04</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">0.77</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
    <td align="right">1.11</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.01</td>
    <td align="right">1.16</td>
    <td align="right">1.18</td>
    <td align="right">1.20</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.02</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="right">1.15</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">0.98</td>
    <td align="right">0.83</td>
    <td align="right">0.82</td>
    <td align="right">0.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">0.82</td>
    <td align="right">1.09</td>
    <td align="right">1.09</td>
    <td align="right">1.09</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">0.98</td>
    <td align="right">1.06</td>
    <td align="right">1.06</td>
    <td align="right">1.04</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">0.94</td>
    <td align="right">0.82</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">0.98</td>
    <td align="right">1.13</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">1.04</td>
    <td align="right">1.05</td>
    <td align="right">1.03</td>
    <td align="right">1.05</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
    <td align="right">1.07</td>
    <td align="right">1.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">1.00</td>
    <td align="right">1.10</td>
    <td align="right">1.08</td>
    <td align="right">1.11</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">0.94</td>
    <td align="right">0.94</td>
    <td align="right">0.93</td>
    <td align="right">0.95</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.06</td>
    <td align="right">1.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">0.96</td>
    <td align="right">0.82</td>
    <td align="right">0.82</td>
    <td align="right">0.82</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">0.94</td>
    <td align="right">0.94</td>
    <td align="right">0.94</td>
    <td align="right">0.94</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">1.01</td>
    <td align="right">0.94</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">0.97</td>
    <td align="right">0.84</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">0.82</td>
    <td align="right">0.90</td>
    <td align="right">0.90</td>
    <td align="right">0.90</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">0.99</td>
    <td align="right">0.96</td>
    <td align="right">0.95</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">1.00</td>
    <td align="right">0.97</td>
    <td align="right">1.05</td>
    <td align="right">1.08</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">0.85</td>
    <td align="right">0.91</td>
    <td align="right">1.04</td>
    <td align="right">1.01</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">0.92</td>
    <td align="right">0.91</td>
    <td align="right">0.94</td>
    <td align="right">1.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">1.00</td>
    <td align="right">0.98</td>
    <td align="right">1.04</td>
    <td align="right">1.05</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">0.89</td>
    <td align="right">0.90</td>
    <td align="right">0.96</td>
    <td align="right">1.00</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">0.94</td>
    <td align="right">0.89</td>
    <td align="right">0.93</td>
    <td align="right">0.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">1.25</td>
    <td align="right">1.41</td>
    <td align="right">1.10</td>
    <td align="right">1.25</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">0.83</td>
    <td align="right">1.35</td>
    <td align="right">1.11</td>
    <td align="right">1.25</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">1.02</td>
    <td align="right">1.24</td>
    <td align="right">1.26</td>
    <td align="right">1.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">1.38</td>
    <td align="right">1.51</td>
    <td align="right">1.16</td>
    <td align="right">1.40</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">0.90</td>
    <td align="right">1.37</td>
    <td align="right">1.11</td>
    <td align="right">1.22</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">1.01</td>
    <td align="right">1.17</td>
    <td align="right">1.22</td>
    <td align="right">1.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">1.53</td>
    <td align="right">1.50</td>
    <td align="right">1.08</td>
    <td align="right">1.40</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">1.00</td>
    <td align="right">1.45</td>
    <td align="right">1.14</td>
    <td align="right">1.35</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">0.98</td>
    <td align="right">1.19</td>
    <td align="right">1.13</td>
    <td align="right">1.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">1.46</td>
    <td align="right">1.50</td>
    <td align="right">1.12</td>
    <td align="right">1.46</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">1.10</td>
    <td align="right">1.43</td>
    <td align="right">1.13</td>
    <td align="right">1.38</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">0.92</td>
    <td align="right">1.10</td>
    <td align="right">1.11</td>
    <td align="right">1.09</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">51.90</td>
    <td align="right">23.36</td>
    <td align="right">14.45</td>
    <td align="right">31.29</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">1.04</td>
    <td align="right">1.03</td>
    <td align="right">1.32</td>
    <td align="right">1.24</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.23</td>
    <td align="right">1.85</td>
    <td align="right">1.82</td>
    <td align="right">1.80</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.07</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="right">1.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">1.34</td>
    <td align="right">1.30</td>
    <td align="right">0.67</td>
    <td align="right">1.02</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">1.40</td>
    <td align="right">1.89</td>
    <td align="right">1.88</td>
    <td align="right">1.88</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">1.32</td>
    <td align="right">1.86</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">1.44</td>
    <td align="right">1.42</td>
    <td align="right">0.53</td>
    <td align="right">1.01</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">1.68</td>
    <td align="right">2.22</td>
    <td align="right">2.21</td>
    <td align="right">2.21</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">1.48</td>
    <td align="right">2.09</td>
    <td align="right">2.09</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">1.36</td>
    <td align="right">1.43</td>
    <td align="right">0.44</td>
    <td align="right">0.98</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">1.80</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">1.37</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">1.24</td>
    <td align="right">1.45</td>
    <td align="right">1.44</td>
    <td align="right">1.44</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">1.12</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">0.98</td>
    <td align="right">0.90</td>
    <td align="right">0.89</td>
    <td align="right">0.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">1.23</td>
    <td align="right">1.24</td>
    <td align="right">1.25</td>
    <td align="right">1.24</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">1.31</td>
    <td align="right">1.38</td>
    <td align="right">1.39</td>
    <td align="right">1.38</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">1.08</td>
    <td align="right">1.00</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">1.35</td>
    <td align="right">1.36</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">1.32</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">1.31</td>
    <td align="right">1.44</td>
    <td align="right">1.27</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">1.33</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">1.33</td>
    <td align="right">1.28</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">1.23</td>
    <td align="right">1.43</td>
    <td align="right">1.23</td>
    <td align="right">1.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">0.99</td>
    <td align="right">0.89</td>
    <td align="right">0.89</td>
    <td align="right">0.90</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">0.96</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">0.89</td>
    <td align="right">0.92</td>
    <td align="right">0.91</td>
    <td align="right">0.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">1.14</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">1.22</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">1.25</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">1.24</td>
    <td align="right">1.45</td>
    <td align="right">1.25</td>
    <td align="right">1.28</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">1.39</td>
    <td align="right">1.46</td>
    <td align="right">1.34</td>
    <td align="right">1.25</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">1.30</td>
    <td align="right">1.46</td>
    <td align="right">1.34</td>
    <td align="right">1.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">1.16</td>
    <td align="right">1.44</td>
    <td align="right">1.21</td>
    <td align="right">1.26</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">1.28</td>
    <td align="right">1.55</td>
    <td align="right">1.35</td>
    <td align="right">1.29</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">1.29</td>
    <td align="right">1.42</td>
    <td align="right">1.35</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">1.44</td>
    <td align="right">1.56</td>
    <td align="right">1.20</td>
    <td align="right">1.47</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">0.85</td>
    <td align="right">1.22</td>
    <td align="right">1.15</td>
    <td align="right">1.33</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">1.02</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">1.74</td>
    <td align="right">1.70</td>
    <td align="right">1.32</td>
    <td align="right">1.70</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">1.33</td>
    <td align="right">1.77</td>
    <td align="right">1.23</td>
    <td align="right">1.58</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">1.14</td>
    <td align="right">1.33</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">2.25</td>
    <td align="right">2.15</td>
    <td align="right">1.34</td>
    <td align="right">1.90</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">1.79</td>
    <td align="right">2.09</td>
    <td align="right">1.31</td>
    <td align="right">1.80</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">1.13</td>
    <td align="right">1.45</td>
    <td align="right">1.44</td>
    <td align="right">1.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">2.79</td>
    <td align="right">2.41</td>
    <td align="right">1.39</td>
    <td align="right">2.21</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">2.28</td>
    <td align="right">2.01</td>
    <td align="right">1.31</td>
    <td align="right">1.97</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">1.07</td>
    <td align="right">1.35</td>
    <td align="right">1.38</td>
    <td align="right">1.34</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.53</td>
    <td align="right">2.52</td>
    <td align="right">1.97</td>
    <td align="right">9.33</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">1.13</td>
    <td align="right">0.70</td>
    <td align="right">1.95</td>
    <td align="right">1.50</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">0.80</td>
    <td align="right">0.70</td>
    <td align="right">0.69</td>
    <td align="right">0.70</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">0.81</td>
    <td align="right">0.85</td>
    <td align="right">0.85</td>
    <td align="right">0.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">1.13</td>
    <td align="right">0.71</td>
    <td align="right">1.39</td>
    <td align="right">1.22</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">0.74</td>
    <td align="right">0.78</td>
    <td align="right">0.78</td>
    <td align="right">0.78</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">0.82</td>
    <td align="right">0.87</td>
    <td align="right">0.87</td>
    <td align="right">0.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">1.12</td>
    <td align="right">0.70</td>
    <td align="right">1.07</td>
    <td align="right">1.06</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">0.79</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">0.81</td>
    <td align="right">0.85</td>
    <td align="right">0.85</td>
    <td align="right">0.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">1.14</td>
    <td align="right">0.70</td>
    <td align="right">0.86</td>
    <td align="right">0.94</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">0.83</td>
    <td align="right">0.85</td>
    <td align="right">0.85</td>
    <td align="right">0.85</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">0.81</td>
    <td align="right">0.78</td>
    <td align="right">0.78</td>
    <td align="right">0.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
    <td align="right">0.86</td>
    <td align="right">0.86</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">0.93</td>
    <td align="right">0.93</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">0.92</td>
    <td align="right">0.84</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">0.93</td>
    <td align="right">0.72</td>
    <td align="right">0.72</td>
    <td align="right">0.72</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">0.96</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="right">0.93</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">0.81</td>
    <td align="right">0.71</td>
    <td align="right">0.70</td>
    <td align="right">0.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">1.00</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">0.91</td>
    <td align="right">0.87</td>
    <td align="right">0.86</td>
    <td align="right">1.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">1.01</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">0.97</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">0.91</td>
    <td align="right">0.91</td>
    <td align="right">0.86</td>
    <td align="right">1.16</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">0.94</td>
    <td align="right">0.87</td>
    <td align="right">0.87</td>
    <td align="right">0.87</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">0.88</td>
    <td align="right">0.86</td>
    <td align="right">0.87</td>
    <td align="right">0.88</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">0.91</td>
    <td align="right">0.91</td>
    <td align="right">0.92</td>
    <td align="right">0.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">0.94</td>
    <td align="right">0.90</td>
    <td align="right">0.90</td>
    <td align="right">0.90</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">0.92</td>
    <td align="right">0.72</td>
    <td align="right">0.72</td>
    <td align="right">0.72</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">0.96</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">0.93</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="right">1.18</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">0.97</td>
    <td align="right">0.99</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">0.99</td>
    <td align="right">1.04</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">0.93</td>
    <td align="right">0.92</td>
    <td align="right">0.89</td>
    <td align="right">1.17</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">1.01</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="right">1.00</td>
    <td align="right">0.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">0.97</td>
    <td align="right">1.28</td>
    <td align="right">1.22</td>
    <td align="right">1.35</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">1.16</td>
    <td align="right">1.21</td>
    <td align="right">1.12</td>
    <td align="right">1.17</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">1.00</td>
    <td align="right">0.86</td>
    <td align="right">0.86</td>
    <td align="right">0.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">0.97</td>
    <td align="right">1.34</td>
    <td align="right">1.25</td>
    <td align="right">1.39</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">1.13</td>
    <td align="right">1.26</td>
    <td align="right">1.10</td>
    <td align="right">1.22</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">0.97</td>
    <td align="right">0.78</td>
    <td align="right">0.78</td>
    <td align="right">0.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">1.03</td>
    <td align="right">1.38</td>
    <td align="right">1.25</td>
    <td align="right">1.40</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">1.04</td>
    <td align="right">1.33</td>
    <td align="right">1.11</td>
    <td align="right">1.26</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">0.97</td>
    <td align="right">0.77</td>
    <td align="right">0.78</td>
    <td align="right">0.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">1.07</td>
    <td align="right">1.42</td>
    <td align="right">1.24</td>
    <td align="right">1.48</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">1.02</td>
    <td align="right">1.35</td>
    <td align="right">1.10</td>
    <td align="right">1.27</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">0.99</td>
    <td align="right">0.76</td>
    <td align="right">0.76</td>
    <td align="right">0.76</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.54</td>
    <td align="right">11.28</td>
    <td align="right">6.17</td>
    <td align="right">15.48</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">1.15</td>
    <td align="right">0.82</td>
    <td align="right">1.73</td>
    <td align="right">1.38</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.08</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">0.93</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">1.12</td>
    <td align="right">0.76</td>
    <td align="right">1.11</td>
    <td align="right">1.03</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">1.08</td>
    <td align="right">1.11</td>
    <td align="right">1.23</td>
    <td align="right">1.30</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">1.09</td>
    <td align="right">1.11</td>
    <td align="right">1.08</td>
    <td align="right">1.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">1.04</td>
    <td align="right">0.79</td>
    <td align="right">0.59</td>
    <td align="right">0.70</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">1.23</td>
    <td align="right">1.39</td>
    <td align="right">1.34</td>
    <td align="right">1.38</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">1.28</td>
    <td align="right">1.27</td>
    <td align="right">1.22</td>
    <td align="right">1.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">1.13</td>
    <td align="right">0.79</td>
    <td align="right">0.41</td>
    <td align="right">0.60</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">1.21</td>
    <td align="right">1.59</td>
    <td align="right">1.54</td>
    <td align="right">1.55</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">1.09</td>
    <td align="right">1.07</td>
    <td align="right">1.04</td>
    <td align="right">1.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">0.95</td>
    <td align="right">1.04</td>
    <td align="right">1.06</td>
    <td align="right">1.06</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">0.98</td>
    <td align="right">1.09</td>
    <td align="right">1.09</td>
    <td align="right">1.07</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">0.99</td>
    <td align="right">1.04</td>
    <td align="right">1.06</td>
    <td align="right">1.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">1.09</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
    <td align="right">1.13</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">1.20</td>
    <td align="right">1.19</td>
    <td align="right">1.18</td>
    <td align="right">1.22</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">1.10</td>
    <td align="right">1.24</td>
    <td align="right">1.06</td>
    <td align="right">1.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">1.32</td>
    <td align="right">1.28</td>
    <td align="right">1.31</td>
    <td align="right">1.32</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">1.37</td>
    <td align="right">1.32</td>
    <td align="right">1.23</td>
    <td align="right">1.31</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">1.35</td>
    <td align="right">1.31</td>
    <td align="right">1.18</td>
    <td align="right">1.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">1.36</td>
    <td align="right">1.26</td>
    <td align="right">1.26</td>
    <td align="right">1.27</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">1.33</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="right">1.29</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">1.23</td>
    <td align="right">1.22</td>
    <td align="right">1.10</td>
    <td align="right">1.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">0.98</td>
    <td align="right">1.05</td>
    <td align="right">1.05</td>
    <td align="right">1.04</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">0.95</td>
    <td align="right">1.05</td>
    <td align="right">1.06</td>
    <td align="right">1.05</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">0.97</td>
    <td align="right">1.09</td>
    <td align="right">1.09</td>
    <td align="right">1.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">1.04</td>
    <td align="right">0.97</td>
    <td align="right">1.02</td>
    <td align="right">1.00</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">1.26</td>
    <td align="right">1.18</td>
    <td align="right">1.17</td>
    <td align="right">1.18</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">1.17</td>
    <td align="right">1.19</td>
    <td align="right">1.16</td>
    <td align="right">1.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">1.27</td>
    <td align="right">1.27</td>
    <td align="right">1.10</td>
    <td align="right">1.17</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">1.33</td>
    <td align="right">1.32</td>
    <td align="right">1.31</td>
    <td align="right">1.32</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">1.33</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
    <td align="right">1.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="right">1.12</td>
    <td align="right">1.16</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">1.32</td>
    <td align="right">1.25</td>
    <td align="right">1.26</td>
    <td align="right">1.27</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">1.32</td>
    <td align="right">1.29</td>
    <td align="right">1.30</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">1.26</td>
    <td align="right">1.47</td>
    <td align="right">1.31</td>
    <td align="right">1.53</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">1.36</td>
    <td align="right">1.35</td>
    <td align="right">1.15</td>
    <td align="right">1.26</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">1.02</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">1.54</td>
    <td align="right">1.65</td>
    <td align="right">1.37</td>
    <td align="right">1.66</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">1.65</td>
    <td align="right">1.49</td>
    <td align="right">1.19</td>
    <td align="right">1.48</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">1.13</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="right">1.32</td>
    <td align="right">1.65</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">1.71</td>
    <td align="right">1.60</td>
    <td align="right">1.21</td>
    <td align="right">1.61</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">1.47</td>
    <td align="right">1.44</td>
    <td align="right">1.45</td>
    <td align="right">1.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">1.79</td>
    <td align="right">1.70</td>
    <td align="right">1.27</td>
    <td align="right">1.71</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">1.88</td>
    <td align="right">1.79</td>
    <td align="right">1.19</td>
    <td align="right">1.70</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">1.67</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">24.44</td>
    <td align="right">5.21</td>
    <td align="right">3.55</td>
    <td align="right">10.01</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">1.11</td>
    <td align="right">1.13</td>
    <td align="right">1.42</td>
    <td align="right">1.36</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.40</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="right">1.16</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.34</td>
    <td align="right">1.18</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">1.07</td>
    <td align="right">1.11</td>
    <td align="right">1.03</td>
    <td align="right">1.14</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.39</td>
    <td align="right">1.25</td>
    <td align="right">1.23</td>
    <td align="right">1.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">1.05</td>
    <td align="right">1.14</td>
    <td align="right">0.79</td>
    <td align="right">1.09</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.46</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
    <td align="right">1.15</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.43</td>
    <td align="right">1.23</td>
    <td align="right">1.22</td>
    <td align="right">1.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">1.04</td>
    <td align="right">1.13</td>
    <td align="right">0.65</td>
    <td align="right">1.00</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.48</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.46</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.47</td>
    <td align="right">1.16</td>
    <td align="right">1.32</td>
    <td align="right">1.31</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">0.91</td>
    <td align="right">1.25</td>
    <td align="right">1.26</td>
    <td align="right">1.26</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">0.98</td>
    <td align="right">0.59</td>
    <td align="right">0.59</td>
    <td align="right">0.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">1.62</td>
    <td align="right">1.45</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">1.04</td>
    <td align="right">1.33</td>
    <td align="right">1.33</td>
    <td align="right">1.32</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">0.97</td>
    <td align="right">0.74</td>
    <td align="right">0.62</td>
    <td align="right">0.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">1.47</td>
    <td align="right">1.49</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">0.98</td>
    <td align="right">1.56</td>
    <td align="right">1.55</td>
    <td align="right">1.50</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">1.08</td>
    <td align="right">0.94</td>
    <td align="right">0.74</td>
    <td align="right">0.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">1.44</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">1.09</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="right">1.53</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">1.08</td>
    <td align="right">0.94</td>
    <td align="right">0.75</td>
    <td align="right">1.00</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">0.90</td>
    <td align="right">0.57</td>
    <td align="right">0.57</td>
    <td align="right">0.57</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">1.01</td>
    <td align="right">0.75</td>
    <td align="right">0.75</td>
    <td align="right">0.75</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">0.99</td>
    <td align="right">0.74</td>
    <td align="right">0.74</td>
    <td align="right">0.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.01</td>
    <td align="right">0.81</td>
    <td align="right">0.69</td>
    <td align="right">0.88</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">1.03</td>
    <td align="right">0.84</td>
    <td align="right">0.73</td>
    <td align="right">0.83</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">1.08</td>
    <td align="right">0.94</td>
    <td align="right">0.84</td>
    <td align="right">0.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">1.08</td>
    <td align="right">0.92</td>
    <td align="right">0.72</td>
    <td align="right">0.92</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">1.14</td>
    <td align="right">1.04</td>
    <td align="right">0.97</td>
    <td align="right">1.02</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">1.07</td>
    <td align="right">1.03</td>
    <td align="right">0.97</td>
    <td align="right">0.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">1.08</td>
    <td align="right">0.91</td>
    <td align="right">0.72</td>
    <td align="right">0.93</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">1.03</td>
    <td align="right">1.00</td>
    <td align="right">0.97</td>
    <td align="right">0.98</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">1.04</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="right">1.11</td>
    <td align="right">1.33</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">1.00</td>
    <td align="right">1.39</td>
    <td align="right">1.13</td>
    <td align="right">1.34</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">1.10</td>
    <td align="right">1.08</td>
    <td align="right">1.09</td>
    <td align="right">1.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">1.31</td>
    <td align="right">1.38</td>
    <td align="right">1.16</td>
    <td align="right">1.33</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">1.06</td>
    <td align="right">1.51</td>
    <td align="right">1.16</td>
    <td align="right">1.36</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">1.06</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">1.32</td>
    <td align="right">1.27</td>
    <td align="right">1.15</td>
    <td align="right">1.37</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">1.25</td>
    <td align="right">1.52</td>
    <td align="right">1.12</td>
    <td align="right">1.42</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">0.94</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">1.31</td>
    <td align="right">1.30</td>
    <td align="right">1.17</td>
    <td align="right">1.46</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">1.26</td>
    <td align="right">1.43</td>
    <td align="right">1.09</td>
    <td align="right">1.40</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">0.96</td>
    <td align="right">0.97</td>
    <td align="right">0.95</td>
    <td align="right">0.94</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.28</td>
    <td align="right">24.74</td>
    <td align="right">17.96</td>
    <td align="right">28.90</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">1.10</td>
    <td align="right">1.17</td>
    <td align="right">1.56</td>
    <td align="right">1.49</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">0.52</td>
    <td align="right">1.16</td>
    <td align="right">1.21</td>
    <td align="right">1.21</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.43</td>
    <td align="right">1.30</td>
    <td align="right">1.29</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">1.11</td>
    <td align="right">1.20</td>
    <td align="right">1.07</td>
    <td align="right">1.13</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">1.79</td>
    <td align="right">1.16</td>
    <td align="right">1.10</td>
    <td align="right">1.11</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">1.31</td>
    <td align="right">1.30</td>
    <td align="right">1.21</td>
    <td align="right">1.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">1.60</td>
    <td align="right">1.75</td>
    <td align="right">0.57</td>
    <td align="right">1.21</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">1.96</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">1.84</td>
    <td align="right">1.88</td>
    <td align="right">1.86</td>
    <td align="right">1.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">1.61</td>
    <td align="right">1.88</td>
    <td align="right">0.50</td>
    <td align="right">1.23</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">2.15</td>
    <td align="right">2.06</td>
    <td align="right">2.06</td>
    <td align="right">2.06</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">2.14</td>
    <td align="right">2.41</td>
    <td align="right">2.41</td>
    <td align="right">2.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">0.81</td>
    <td align="right">1.25</td>
    <td align="right">1.37</td>
    <td align="right">1.31</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">0.99</td>
    <td align="right">1.29</td>
    <td align="right">1.33</td>
    <td align="right">1.33</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">1.00</td>
    <td align="right">0.60</td>
    <td align="right">0.60</td>
    <td align="right">0.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">1.57</td>
    <td align="right">1.45</td>
    <td align="right">1.38</td>
    <td align="right">1.40</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">1.13</td>
    <td align="right">1.49</td>
    <td align="right">1.39</td>
    <td align="right">1.28</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">0.72</td>
    <td align="right">1.41</td>
    <td align="right">1.34</td>
    <td align="right">1.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">2.29</td>
    <td align="right">2.12</td>
    <td align="right">2.13</td>
    <td align="right">2.11</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">1.86</td>
    <td align="right">2.01</td>
    <td align="right">1.99</td>
    <td align="right">1.98</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">1.49</td>
    <td align="right">1.64</td>
    <td align="right">1.22</td>
    <td align="right">1.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.06</td>
    <td align="right">1.97</td>
    <td align="right">1.95</td>
    <td align="right">1.95</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">1.89</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">1.68</td>
    <td align="right">1.71</td>
    <td align="right">1.24</td>
    <td align="right">1.33</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.41</td>
    <td align="right">0.60</td>
    <td align="right">0.58</td>
    <td align="right">0.52</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">1.03</td>
    <td align="right">0.78</td>
    <td align="right">0.78</td>
    <td align="right">0.72</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">0.69</td>
    <td align="right">0.74</td>
    <td align="right">0.77</td>
    <td align="right">0.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">1.02</td>
    <td align="right">0.98</td>
    <td align="right">0.86</td>
    <td align="right">0.97</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">1.51</td>
    <td align="right">0.98</td>
    <td align="right">0.87</td>
    <td align="right">0.93</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">0.97</td>
    <td align="right">0.49</td>
    <td align="right">0.47</td>
    <td align="right">0.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">1.71</td>
    <td align="right">1.63</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">2.03</td>
    <td align="right">1.68</td>
    <td align="right">1.51</td>
    <td align="right">1.38</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">1.58</td>
    <td align="right">1.66</td>
    <td align="right">1.50</td>
    <td align="right">1.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">1.78</td>
    <td align="right">1.72</td>
    <td align="right">1.24</td>
    <td align="right">1.31</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">1.95</td>
    <td align="right">1.79</td>
    <td align="right">1.45</td>
    <td align="right">1.40</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">1.88</td>
    <td align="right">1.74</td>
    <td align="right">1.42</td>
    <td align="right">1.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">1.47</td>
    <td align="right">1.49</td>
    <td align="right">1.20</td>
    <td align="right">1.49</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">1.05</td>
    <td align="right">1.49</td>
    <td align="right">1.18</td>
    <td align="right">1.49</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">1.13</td>
    <td align="right">1.03</td>
    <td align="right">1.06</td>
    <td align="right">1.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">1.22</td>
    <td align="right">1.46</td>
    <td align="right">1.26</td>
    <td align="right">1.42</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">1.09</td>
    <td align="right">1.59</td>
    <td align="right">1.21</td>
    <td align="right">1.51</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">1.06</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">2.17</td>
    <td align="right">2.21</td>
    <td align="right">1.51</td>
    <td align="right">2.03</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">2.17</td>
    <td align="right">2.30</td>
    <td align="right">1.33</td>
    <td align="right">2.09</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">1.12</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">2.40</td>
    <td align="right">2.43</td>
    <td align="right">1.62</td>
    <td align="right">2.47</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">2.28</td>
    <td align="right">2.45</td>
    <td align="right">1.40</td>
    <td align="right">2.34</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.28</td>
    <td align="right">34.05</td>
    <td align="right">14.25</td>
    <td align="right">28.53</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">0.93</td>
    <td align="right">0.83</td>
    <td align="right">0.74</td>
    <td align="right">0.79</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">0.89</td>
    <td align="right">0.74</td>
    <td align="right">0.74</td>
    <td align="right">0.73</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">0.81</td>
    <td align="right">0.77</td>
    <td align="right">0.75</td>
    <td align="right">0.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">0.89</td>
    <td align="right">0.85</td>
    <td align="right">0.51</td>
    <td align="right">0.67</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">0.88</td>
    <td align="right">0.78</td>
    <td align="right">0.78</td>
    <td align="right">0.77</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">0.87</td>
    <td align="right">0.64</td>
    <td align="right">0.64</td>
    <td align="right">0.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">0.81</td>
    <td align="right">0.84</td>
    <td align="right">0.40</td>
    <td align="right">0.63</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">0.92</td>
    <td align="right">0.70</td>
    <td align="right">0.70</td>
    <td align="right">0.68</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">0.87</td>
    <td align="right">0.63</td>
    <td align="right">0.61</td>
    <td align="right">0.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">0.90</td>
    <td align="right">0.79</td>
    <td align="right">0.32</td>
    <td align="right">0.58</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">0.92</td>
    <td align="right">0.64</td>
    <td align="right">0.65</td>
    <td align="right">0.65</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">0.90</td>
    <td align="right">0.57</td>
    <td align="right">0.55</td>
    <td align="right">0.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">1.10</td>
    <td align="right">0.45</td>
    <td align="right">0.47</td>
    <td align="right">0.46</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">0.92</td>
    <td align="right">0.93</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">0.93</td>
    <td align="right">0.83</td>
    <td align="right">0.84</td>
    <td align="right">0.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">1.28</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">0.97</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">0.93</td>
    <td align="right">0.85</td>
    <td align="right">0.90</td>
    <td align="right">0.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">1.03</td>
    <td align="right">0.65</td>
    <td align="right">0.66</td>
    <td align="right">0.66</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">1.02</td>
    <td align="right">0.70</td>
    <td align="right">0.71</td>
    <td align="right">0.71</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">0.97</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">0.99</td>
    <td align="right">0.68</td>
    <td align="right">0.68</td>
    <td align="right">0.68</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">1.03</td>
    <td align="right">0.74</td>
    <td align="right">0.75</td>
    <td align="right">0.75</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">0.95</td>
    <td align="right">0.91</td>
    <td align="right">0.90</td>
    <td align="right">0.91</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">0.86</td>
    <td align="right">0.83</td>
    <td align="right">0.81</td>
    <td align="right">0.81</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">1.11</td>
    <td align="right">0.46</td>
    <td align="right">0.46</td>
    <td align="right">0.46</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">0.93</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">0.88</td>
    <td align="right">0.86</td>
    <td align="right">0.86</td>
    <td align="right">0.85</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">1.29</td>
    <td align="right">0.97</td>
    <td align="right">0.96</td>
    <td align="right">0.97</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">0.97</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">0.89</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">1.04</td>
    <td align="right">0.65</td>
    <td align="right">0.66</td>
    <td align="right">0.66</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">1.01</td>
    <td align="right">0.70</td>
    <td align="right">0.71</td>
    <td align="right">0.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">0.90</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
    <td align="right">0.94</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">1.01</td>
    <td align="right">0.68</td>
    <td align="right">0.68</td>
    <td align="right">0.68</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">1.03</td>
    <td align="right">0.75</td>
    <td align="right">0.75</td>
    <td align="right">0.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">0.93</td>
    <td align="right">0.52</td>
    <td align="right">0.76</td>
    <td align="right">0.66</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">0.98</td>
    <td align="right">0.49</td>
    <td align="right">0.81</td>
    <td align="right">0.61</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">0.85</td>
    <td align="right">0.72</td>
    <td align="right">0.72</td>
    <td align="right">0.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">0.92</td>
    <td align="right">0.99</td>
    <td align="right">0.97</td>
    <td align="right">0.96</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">0.96</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">0.94</td>
    <td align="right">0.73</td>
    <td align="right">0.73</td>
    <td align="right">0.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">0.94</td>
    <td align="right">0.98</td>
    <td align="right">0.97</td>
    <td align="right">0.93</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">0.90</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">0.96</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">0.95</td>
    <td align="right">0.76</td>
    <td align="right">0.74</td>
    <td align="right">0.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">0.96</td>
    <td align="right">0.92</td>
    <td align="right">0.97</td>
    <td align="right">0.92</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">0.92</td>
    <td align="right">0.99</td>
    <td align="right">1.00</td>
    <td align="right">0.96</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">0.98</td>
    <td align="right">0.78</td>
    <td align="right">0.80</td>
    <td align="right">0.78</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">108.60</td>
    <td align="right">129.69</td>
    <td align="right">28.42</td>
    <td align="right">85.18</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">0.90</td>
    <td align="right">0.83</td>
    <td align="right">0.72</td>
    <td align="right">0.77</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">0.93</td>
    <td align="right">0.80</td>
    <td align="right">0.79</td>
    <td align="right">0.80</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">0.81</td>
    <td align="right">0.76</td>
    <td align="right">0.74</td>
    <td align="right">0.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">0.92</td>
    <td align="right">0.94</td>
    <td align="right">0.42</td>
    <td align="right">0.66</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">0.86</td>
    <td align="right">0.81</td>
    <td align="right">0.80</td>
    <td align="right">0.81</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">0.89</td>
    <td align="right">0.73</td>
    <td align="right">0.74</td>
    <td align="right">0.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">0.94</td>
    <td align="right">0.96</td>
    <td align="right">0.32</td>
    <td align="right">0.68</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">0.96</td>
    <td align="right">0.95</td>
    <td align="right">0.93</td>
    <td align="right">0.99</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">0.93</td>
    <td align="right">0.90</td>
    <td align="right">0.90</td>
    <td align="right">0.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">1.00</td>
    <td align="right">0.96</td>
    <td align="right">0.25</td>
    <td align="right">0.60</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">0.96</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">1.21</td>
    <td align="right">0.84</td>
    <td align="right">0.82</td>
    <td align="right">0.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">1.06</td>
    <td align="right">0.51</td>
    <td align="right">0.51</td>
    <td align="right">0.51</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">0.92</td>
    <td align="right">0.97</td>
    <td align="right">0.99</td>
    <td align="right">0.98</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">0.90</td>
    <td align="right">0.94</td>
    <td align="right">0.95</td>
    <td align="right">0.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">1.32</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">0.98</td>
    <td align="right">0.89</td>
    <td align="right">0.88</td>
    <td align="right">0.89</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">0.97</td>
    <td align="right">0.96</td>
    <td align="right">0.95</td>
    <td align="right">0.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">1.02</td>
    <td align="right">0.83</td>
    <td align="right">0.81</td>
    <td align="right">0.81</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">1.01</td>
    <td align="right">0.80</td>
    <td align="right">0.80</td>
    <td align="right">0.80</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">1.10</td>
    <td align="right">0.95</td>
    <td align="right">0.96</td>
    <td align="right">0.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">1.02</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">1.02</td>
    <td align="right">0.84</td>
    <td align="right">0.84</td>
    <td align="right">0.84</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">1.16</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">0.87</td>
    <td align="right">0.84</td>
    <td align="right">0.84</td>
    <td align="right">0.82</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">1.15</td>
    <td align="right">0.54</td>
    <td align="right">0.54</td>
    <td align="right">0.53</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">0.94</td>
    <td align="right">0.99</td>
    <td align="right">0.98</td>
    <td align="right">0.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">0.92</td>
    <td align="right">0.90</td>
    <td align="right">0.90</td>
    <td align="right">0.89</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">1.31</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">0.98</td>
    <td align="right">0.93</td>
    <td align="right">0.94</td>
    <td align="right">0.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">0.95</td>
    <td align="right">1.12</td>
    <td align="right">1.09</td>
    <td align="right">1.11</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">1.02</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">1.01</td>
    <td align="right">0.80</td>
    <td align="right">0.80</td>
    <td align="right">0.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">0.98</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">1.03</td>
    <td align="right">0.86</td>
    <td align="right">0.86</td>
    <td align="right">0.86</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">1.02</td>
    <td align="right">0.85</td>
    <td align="right">0.85</td>
    <td align="right">0.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">0.91</td>
    <td align="right">0.58</td>
    <td align="right">0.78</td>
    <td align="right">0.72</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">1.02</td>
    <td align="right">0.60</td>
    <td align="right">0.89</td>
    <td align="right">0.71</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">0.86</td>
    <td align="right">0.78</td>
    <td align="right">0.76</td>
    <td align="right">0.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">0.93</td>
    <td align="right">1.00</td>
    <td align="right">1.08</td>
    <td align="right">0.98</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">0.97</td>
    <td align="right">1.01</td>
    <td align="right">1.04</td>
    <td align="right">1.01</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">0.91</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">0.94</td>
    <td align="right">0.97</td>
    <td align="right">1.10</td>
    <td align="right">0.96</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">0.94</td>
    <td align="right">1.03</td>
    <td align="right">1.08</td>
    <td align="right">1.02</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">0.98</td>
    <td align="right">0.91</td>
    <td align="right">0.90</td>
    <td align="right">0.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
    <td align="right">1.14</td>
    <td align="right">0.97</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">0.96</td>
    <td align="right">0.98</td>
    <td align="right">1.11</td>
    <td align="right">0.99</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">0.98</td>
    <td align="right">0.94</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">79.13</td>
    <td align="right">13.82</td>
    <td align="right">8.55</td>
    <td align="right">18.00</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">0.91</td>
    <td align="right">0.76</td>
    <td align="right">0.78</td>
    <td align="right">0.78</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">0.92</td>
    <td align="right">0.88</td>
    <td align="right">0.87</td>
    <td align="right">0.88</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">0.96</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">0.89</td>
    <td align="right">0.75</td>
    <td align="right">0.55</td>
    <td align="right">0.66</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">0.96</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">0.98</td>
    <td align="right">0.99</td>
    <td align="right">0.98</td>
    <td align="right">1.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">0.92</td>
    <td align="right">0.87</td>
    <td align="right">0.47</td>
    <td align="right">0.71</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">1.01</td>
    <td align="right">1.02</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">1.06</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">1.12</td>
    <td align="right">0.94</td>
    <td align="right">0.37</td>
    <td align="right">0.63</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">1.07</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">1.08</td>
    <td align="right">0.97</td>
    <td align="right">0.96</td>
    <td align="right">0.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">1.01</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">0.95</td>
    <td align="right">1.01</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">0.94</td>
    <td align="right">0.86</td>
    <td align="right">0.86</td>
    <td align="right">0.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">0.96</td>
    <td align="right">1.06</td>
    <td align="right">1.07</td>
    <td align="right">1.06</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">1.06</td>
    <td align="right">1.04</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">1.02</td>
    <td align="right">1.10</td>
    <td align="right">1.10</td>
    <td align="right">1.10</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">0.95</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">1.03</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
    <td align="right">1.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">1.04</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">0.96</td>
    <td align="right">1.05</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">1.06</td>
    <td align="right">1.06</td>
    <td align="right">1.05</td>
    <td align="right">1.06</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">0.90</td>
    <td align="right">0.86</td>
    <td align="right">0.85</td>
    <td align="right">0.85</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.02</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">0.96</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">1.07</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
    <td align="right">1.13</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">0.96</td>
    <td align="right">1.08</td>
    <td align="right">1.06</td>
    <td align="right">1.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">1.08</td>
    <td align="right">1.17</td>
    <td align="right">1.16</td>
    <td align="right">1.18</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">1.02</td>
    <td align="right">1.10</td>
    <td align="right">1.10</td>
    <td align="right">1.10</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">0.95</td>
    <td align="right">1.05</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">0.95</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
    <td align="right">1.06</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">1.03</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">0.96</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">0.97</td>
    <td align="right">1.04</td>
    <td align="right">1.06</td>
    <td align="right">1.02</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">1.01</td>
    <td align="right">0.97</td>
    <td align="right">0.94</td>
    <td align="right">0.93</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">0.97</td>
    <td align="right">1.02</td>
    <td align="right">1.04</td>
    <td align="right">1.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">1.02</td>
    <td align="right">1.06</td>
    <td align="right">1.04</td>
    <td align="right">0.98</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">0.97</td>
    <td align="right">1.02</td>
    <td align="right">0.99</td>
    <td align="right">1.00</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">1.00</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">1.01</td>
    <td align="right">1.03</td>
    <td align="right">1.06</td>
    <td align="right">0.97</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">0.98</td>
    <td align="right">1.04</td>
    <td align="right">0.97</td>
    <td align="right">1.00</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">0.99</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">1.02</td>
    <td align="right">1.04</td>
    <td align="right">1.08</td>
    <td align="right">1.04</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">1.00</td>
    <td align="right">1.02</td>
    <td align="right">1.00</td>
    <td align="right">1.02</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">1.01</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">124.72</td>
    <td align="right">62.05</td>
    <td align="right">23.23</td>
    <td align="right">53.66</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">0.90</td>
    <td align="right">0.77</td>
    <td align="right">0.75</td>
    <td align="right">0.78</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">0.89</td>
    <td align="right">0.82</td>
    <td align="right">0.82</td>
    <td align="right">0.82</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">1.00</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">0.91</td>
    <td align="right">0.83</td>
    <td align="right">0.42</td>
    <td align="right">0.66</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">1.02</td>
    <td align="right">0.96</td>
    <td align="right">0.97</td>
    <td align="right">0.96</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">1.02</td>
    <td align="right">1.07</td>
    <td align="right">1.06</td>
    <td align="right">1.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">0.97</td>
    <td align="right">1.02</td>
    <td align="right">0.34</td>
    <td align="right">0.67</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">1.01</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">1.22</td>
    <td align="right">1.15</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">1.10</td>
    <td align="right">1.04</td>
    <td align="right">0.26</td>
    <td align="right">0.68</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">1.29</td>
    <td align="right">1.22</td>
    <td align="right">1.21</td>
    <td align="right">1.21</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">1.28</td>
    <td align="right">1.00</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">0.99</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">0.95</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="right">1.04</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">0.89</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
    <td align="right">0.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">1.11</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">0.93</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">1.08</td>
    <td align="right">1.08</td>
    <td align="right">1.07</td>
    <td align="right">1.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">1.02</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">0.97</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">1.13</td>
    <td align="right">1.17</td>
    <td align="right">1.17</td>
    <td align="right">1.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">1.01</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">0.98</td>
    <td align="right">1.04</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">1.04</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">0.93</td>
    <td align="right">0.87</td>
    <td align="right">0.87</td>
    <td align="right">0.86</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">1.02</td>
    <td align="right">1.10</td>
    <td align="right">1.08</td>
    <td align="right">1.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">1.09</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="right">1.18</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">1.05</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">0.98</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">1.14</td>
    <td align="right">1.14</td>
    <td align="right">1.13</td>
    <td align="right">1.21</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">1.02</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">0.98</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">0.96</td>
    <td align="right">1.05</td>
    <td align="right">1.05</td>
    <td align="right">1.05</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">0.98</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">0.90</td>
    <td align="right">0.98</td>
    <td align="right">1.04</td>
    <td align="right">1.01</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">1.06</td>
    <td align="right">0.99</td>
    <td align="right">1.05</td>
    <td align="right">1.04</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">0.98</td>
    <td align="right">0.96</td>
    <td align="right">0.97</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">1.07</td>
    <td align="right">1.08</td>
    <td align="right">1.13</td>
    <td align="right">1.04</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">0.99</td>
    <td align="right">1.04</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">0.95</td>
    <td align="right">0.98</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">0.99</td>
    <td align="right">1.00</td>
    <td align="right">1.15</td>
    <td align="right">0.97</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.02</td>
    <td align="right">1.00</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">1.01</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">1.01</td>
    <td align="right">1.02</td>
    <td align="right">1.21</td>
    <td align="right">1.02</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">1.01</td>
    <td align="right">1.03</td>
    <td align="right">1.10</td>
    <td align="right">1.04</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">1.05</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.02</td>
    <td align="right">6.67</td>
    <td align="right">5.58</td>
    <td align="right">12.05</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">1.09</td>
    <td align="right">0.96</td>
    <td align="right">0.63</td>
    <td align="right">0.78</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">1.01</td>
    <td align="right">0.94</td>
    <td align="right">0.92</td>
    <td align="right">0.93</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">1.06</td>
    <td align="right">1.02</td>
    <td align="right">0.98</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">1.16</td>
    <td align="right">0.96</td>
    <td align="right">0.46</td>
    <td align="right">0.71</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">1.01</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.94</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">1.06</td>
    <td align="right">1.00</td>
    <td align="right">0.98</td>
    <td align="right">0.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">1.17</td>
    <td align="right">0.95</td>
    <td align="right">0.37</td>
    <td align="right">0.65</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">0.97</td>
    <td align="right">0.98</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">1.07</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">1.28</td>
    <td align="right">0.97</td>
    <td align="right">0.29</td>
    <td align="right">0.64</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">1.00</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
    <td align="right">0.95</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">1.07</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">1.06</td>
    <td align="right">0.98</td>
    <td align="right">1.00</td>
    <td align="right">0.98</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">1.07</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">0.72</td>
    <td align="right">0.94</td>
    <td align="right">0.93</td>
    <td align="right">0.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">1.13</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">0.99</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">1.14</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
    <td align="right">0.99</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">0.51</td>
    <td align="right">0.95</td>
    <td align="right">0.92</td>
    <td align="right">0.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">1.05</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">1.13</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.02</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">0.63</td>
    <td align="right">1.13</td>
    <td align="right">1.19</td>
    <td align="right">1.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">1.05</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">1.14</td>
    <td align="right">0.99</td>
    <td align="right">1.01</td>
    <td align="right">0.99</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">0.63</td>
    <td align="right">1.14</td>
    <td align="right">1.20</td>
    <td align="right">1.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">0.72</td>
    <td align="right">0.93</td>
    <td align="right">0.93</td>
    <td align="right">0.92</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">0.74</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">0.75</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">0.52</td>
    <td align="right">1.08</td>
    <td align="right">1.11</td>
    <td align="right">1.08</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">0.54</td>
    <td align="right">0.92</td>
    <td align="right">0.90</td>
    <td align="right">0.93</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">0.56</td>
    <td align="right">1.09</td>
    <td align="right">1.13</td>
    <td align="right">1.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">0.65</td>
    <td align="right">1.11</td>
    <td align="right">1.16</td>
    <td align="right">1.13</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">0.67</td>
    <td align="right">1.10</td>
    <td align="right">1.17</td>
    <td align="right">1.12</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">0.68</td>
    <td align="right">1.11</td>
    <td align="right">1.17</td>
    <td align="right">1.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">0.65</td>
    <td align="right">1.13</td>
    <td align="right">1.19</td>
    <td align="right">1.13</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">0.67</td>
    <td align="right">1.12</td>
    <td align="right">1.18</td>
    <td align="right">1.11</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">0.69</td>
    <td align="right">1.11</td>
    <td align="right">1.17</td>
    <td align="right">1.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">1.10</td>
    <td align="right">0.91</td>
    <td align="right">1.01</td>
    <td align="right">0.97</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">1.13</td>
    <td align="right">0.94</td>
    <td align="right">1.05</td>
    <td align="right">0.98</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">1.00</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">1.08</td>
    <td align="right">0.95</td>
    <td align="right">1.01</td>
    <td align="right">0.99</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">1.15</td>
    <td align="right">0.93</td>
    <td align="right">1.03</td>
    <td align="right">1.00</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">1.02</td>
    <td align="right">0.97</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">1.07</td>
    <td align="right">0.95</td>
    <td align="right">1.02</td>
    <td align="right">0.98</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">1.13</td>
    <td align="right">0.94</td>
    <td align="right">1.06</td>
    <td align="right">1.00</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">1.01</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">1.07</td>
    <td align="right">0.93</td>
    <td align="right">1.02</td>
    <td align="right">0.97</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">1.13</td>
    <td align="right">0.92</td>
    <td align="right">1.07</td>
    <td align="right">0.96</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">0.99</td>
    <td align="right">0.96</td>
    <td align="right">0.94</td>
    <td align="right">0.93</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.12</td>
    <td align="right">33.35</td>
    <td align="right">15.60</td>
    <td align="right">36.89</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">1.17</td>
    <td align="right">0.97</td>
    <td align="right">0.66</td>
    <td align="right">0.80</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">1.01</td>
    <td align="right">0.94</td>
    <td align="right">0.93</td>
    <td align="right">0.97</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">1.14</td>
    <td align="right">1.08</td>
    <td align="right">1.03</td>
    <td align="right">0.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">1.23</td>
    <td align="right">0.98</td>
    <td align="right">0.47</td>
    <td align="right">0.73</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">1.07</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="right">1.00</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">1.17</td>
    <td align="right">1.09</td>
    <td align="right">1.08</td>
    <td align="right">1.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">2.26</td>
    <td align="right">1.83</td>
    <td align="right">0.54</td>
    <td align="right">1.19</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">1.45</td>
    <td align="right">1.44</td>
    <td align="right">1.39</td>
    <td align="right">1.36</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">1.69</td>
    <td align="right">1.61</td>
    <td align="right">1.60</td>
    <td align="right">1.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">2.98</td>
    <td align="right">2.30</td>
    <td align="right">0.51</td>
    <td align="right">1.42</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">1.64</td>
    <td align="right">1.56</td>
    <td align="right">1.58</td>
    <td align="right">1.51</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">2.05</td>
    <td align="right">1.99</td>
    <td align="right">1.94</td>
    <td align="right">1.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">1.14</td>
    <td align="right">0.98</td>
    <td align="right">1.00</td>
    <td align="right">0.98</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">1.15</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">0.72</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">1.27</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">1.25</td>
    <td align="right">1.00</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">0.55</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">1.57</td>
    <td align="right">1.17</td>
    <td align="right">1.17</td>
    <td align="right">1.18</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">1.73</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="right">1.23</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">1.08</td>
    <td align="right">1.61</td>
    <td align="right">1.89</td>
    <td align="right">1.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">1.79</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">1.93</td>
    <td align="right">1.29</td>
    <td align="right">1.31</td>
    <td align="right">1.29</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">1.35</td>
    <td align="right">1.85</td>
    <td align="right">2.28</td>
    <td align="right">1.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">0.72</td>
    <td align="right">0.99</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">0.75</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">0.75</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">0.57</td>
    <td align="right">1.17</td>
    <td align="right">1.26</td>
    <td align="right">1.18</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">0.59</td>
    <td align="right">0.96</td>
    <td align="right">0.95</td>
    <td align="right">0.99</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">0.62</td>
    <td align="right">1.16</td>
    <td align="right">1.22</td>
    <td align="right">1.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">1.17</td>
    <td align="right">1.62</td>
    <td align="right">1.94</td>
    <td align="right">1.71</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">1.10</td>
    <td align="right">1.54</td>
    <td align="right">1.83</td>
    <td align="right">1.59</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">1.11</td>
    <td align="right">1.56</td>
    <td align="right">1.85</td>
    <td align="right">1.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">1.39</td>
    <td align="right">1.89</td>
    <td align="right">2.32</td>
    <td align="right">1.97</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">1.27</td>
    <td align="right">1.78</td>
    <td align="right">2.17</td>
    <td align="right">1.84</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">1.29</td>
    <td align="right">1.80</td>
    <td align="right">2.22</td>
    <td align="right">1.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">1.15</td>
    <td align="right">0.91</td>
    <td align="right">1.05</td>
    <td align="right">0.99</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">1.21</td>
    <td align="right">0.95</td>
    <td align="right">1.10</td>
    <td align="right">1.01</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">1.06</td>
    <td align="right">0.95</td>
    <td align="right">0.95</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">1.16</td>
    <td align="right">0.96</td>
    <td align="right">1.08</td>
    <td align="right">1.03</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">1.25</td>
    <td align="right">0.95</td>
    <td align="right">1.11</td>
    <td align="right">1.05</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">1.06</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">1.51</td>
    <td align="right">1.11</td>
    <td align="right">1.51</td>
    <td align="right">1.23</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">1.70</td>
    <td align="right">1.18</td>
    <td align="right">1.71</td>
    <td align="right">1.35</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">1.43</td>
    <td align="right">1.13</td>
    <td align="right">1.13</td>
    <td align="right">1.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">1.60</td>
    <td align="right">1.12</td>
    <td align="right">1.81</td>
    <td align="right">1.31</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">1.85</td>
    <td align="right">1.22</td>
    <td align="right">2.08</td>
    <td align="right">1.44</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">1.13</td>
    <td align="right">1.02</td>
    <td align="right">0.99</td>
    <td align="right">1.00</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
