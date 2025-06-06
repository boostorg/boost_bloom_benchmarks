# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
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
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.21</td>
    <td align="right">4.37</td>
    <td align="right">3.82</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.39</td>
    <td align="right">10.58</td>
    <td align="right">16.60</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.02</td>
    <td align="right">4.34</td>
    <td align="right">4.34</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.82</td>
    <td align="right">5.04</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.47</td>
    <td align="right">15.51</td>
    <td align="right">17.61</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.78</td>
    <td align="right">4.92</td>
    <td align="right">4.95</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.39</td>
    <td align="right">5.47</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.06</td>
    <td align="right">18.66</td>
    <td align="right">16.45</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.38</td>
    <td align="right">5.27</td>
    <td align="right">5.28</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.20</td>
    <td align="right">6.27</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.12</td>
    <td align="right">23.09</td>
    <td align="right">16.70</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.15</td>
    <td align="right">5.86</td>
    <td align="right">5.86</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.66</td>
    <td align="right">6.54</td>
    <td align="right">6.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.03</td>
    <td align="right">5.74</td>
    <td align="right">5.73</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.21</td>
    <td align="right">6.53</td>
    <td align="right">6.47</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.95</td>
    <td align="right">3.24</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.44</td>
    <td align="right">8.81</td>
    <td align="right">8.81</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.10</td>
    <td align="right">9.78</td>
    <td align="right">9.76</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.46</td>
    <td align="right">3.10</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.18</td>
    <td align="right">13.18</td>
    <td align="right">13.17</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.89</td>
    <td align="right">14.92</td>
    <td align="right">14.91</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.67</td>
    <td align="right">5.71</td>
    <td align="right">3.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.99</td>
    <td align="right">14.92</td>
    <td align="right">14.94</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.06</td>
    <td align="right">16.07</td>
    <td align="right">16.16</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.71</td>
    <td align="right">5.75</td>
    <td align="right">3.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.89</td>
    <td align="right">3.18</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.35</td>
    <td align="right">5.03</td>
    <td align="right">4.97</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.55</td>
    <td align="right">4.92</td>
    <td align="right">5.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.03</td>
    <td align="right">3.28</td>
    <td align="right">3.25</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.16</td>
    <td align="right">4.42</td>
    <td align="right">4.42</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.41</td>
    <td align="right">5.03</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.37</td>
    <td align="right">5.43</td>
    <td align="right">3.73</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">6.96</td>
    <td align="right">7.61</td>
    <td align="right">5.82</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.78</td>
    <td align="right">7.43</td>
    <td align="right">5.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.41</td>
    <td align="right">5.44</td>
    <td align="right">3.74</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.97</td>
    <td align="right">8.97</td>
    <td align="right">5.90</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.23</td>
    <td align="right">8.87</td>
    <td align="right">5.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.85</td>
    <td align="right">6.95</td>
    <td align="right">13.52</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.40</td>
    <td align="right">8.87</td>
    <td align="right">17.35</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.54</td>
    <td align="right">10.88</td>
    <td align="right">10.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.24</td>
    <td align="right">8.10</td>
    <td align="right">12.40</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.15</td>
    <td align="right">9.41</td>
    <td align="right">14.27</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.13</td>
    <td align="right">15.40</td>
    <td align="right">15.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.90</td>
    <td align="right">10.30</td>
    <td align="right">12.00</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.26</td>
    <td align="right">12.51</td>
    <td align="right">15.20</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.08</td>
    <td align="right">16.65</td>
    <td align="right">16.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.31</td>
    <td align="right">12.70</td>
    <td align="right">13.14</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.58</td>
    <td align="right">14.05</td>
    <td align="right">14.86</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">21.50</td>
    <td align="right">22.22</td>
    <td align="right">22.27</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">29.81</td>
    <td align="right">16.77</td>
    <td align="right">6.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">12.32</td>
    <td align="right">11.58</td>
    <td align="right">17.10</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.38</td>
    <td align="right">4.66</td>
    <td align="right">4.67</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.28</td>
    <td align="right">5.45</td>
    <td align="right">5.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">17.63</td>
    <td align="right">16.72</td>
    <td align="right">17.67</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.04</td>
    <td align="right">5.13</td>
    <td align="right">5.14</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.70</td>
    <td align="right">5.75</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">23.75</td>
    <td align="right">22.07</td>
    <td align="right">17.00</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.28</td>
    <td align="right">6.11</td>
    <td align="right">6.11</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.98</td>
    <td align="right">7.01</td>
    <td align="right">6.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">35.79</td>
    <td align="right">31.66</td>
    <td align="right">18.07</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.42</td>
    <td align="right">8.83</td>
    <td align="right">13.47</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.20</td>
    <td align="right">8.18</td>
    <td align="right">8.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.48</td>
    <td align="right">6.34</td>
    <td align="right">6.35</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.69</td>
    <td align="right">7.32</td>
    <td align="right">7.25</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.26</td>
    <td align="right">3.64</td>
    <td align="right">3.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.83</td>
    <td align="right">9.36</td>
    <td align="right">9.45</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.14</td>
    <td align="right">9.55</td>
    <td align="right">9.56</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.81</td>
    <td align="right">3.45</td>
    <td align="right">3.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.81</td>
    <td align="right">14.58</td>
    <td align="right">14.04</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.52</td>
    <td align="right">14.95</td>
    <td align="right">15.40</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.80</td>
    <td align="right">6.84</td>
    <td align="right">4.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">13.22</td>
    <td align="right">16.39</td>
    <td align="right">16.29</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.75</td>
    <td align="right">20.66</td>
    <td align="right">20.33</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.02</td>
    <td align="right">13.80</td>
    <td align="right">9.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.26</td>
    <td align="right">3.66</td>
    <td align="right">3.60</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.77</td>
    <td align="right">5.44</td>
    <td align="right">5.39</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.93</td>
    <td align="right">5.33</td>
    <td align="right">5.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.23</td>
    <td align="right">3.55</td>
    <td align="right">3.57</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.56</td>
    <td align="right">4.69</td>
    <td align="right">4.71</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.69</td>
    <td align="right">5.35</td>
    <td align="right">5.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.97</td>
    <td align="right">6.47</td>
    <td align="right">4.64</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">7.86</td>
    <td align="right">8.83</td>
    <td align="right">6.75</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">8.87</td>
    <td align="right">8.77</td>
    <td align="right">6.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.90</td>
    <td align="right">8.65</td>
    <td align="right">5.39</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">10.11</td>
    <td align="right">11.25</td>
    <td align="right">7.65</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">10.05</td>
    <td align="right">11.50</td>
    <td align="right">8.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.57</td>
    <td align="right">7.68</td>
    <td align="right">13.74</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">11.90</td>
    <td align="right">9.50</td>
    <td align="right">17.77</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">11.84</td>
    <td align="right">12.13</td>
    <td align="right">12.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">9.71</td>
    <td align="right">8.46</td>
    <td align="right">12.43</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">12.41</td>
    <td align="right">9.86</td>
    <td align="right">14.36</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">17.52</td>
    <td align="right">17.38</td>
    <td align="right">17.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">12.44</td>
    <td align="right">11.55</td>
    <td align="right">12.97</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">16.86</td>
    <td align="right">13.75</td>
    <td align="right">15.55</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">19.69</td>
    <td align="right">19.89</td>
    <td align="right">19.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">17.72</td>
    <td align="right">16.82</td>
    <td align="right">14.37</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">21.88</td>
    <td align="right">17.18</td>
    <td align="right">15.93</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">27.80</td>
    <td align="right">28.52</td>
    <td align="right">28.52</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.14</td>
    <td align="right">4.45</td>
    <td align="right">3.49</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.60</td>
    <td align="right">8.11</td>
    <td align="right">14.63</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.08</td>
    <td align="right">3.75</td>
    <td align="right">3.85</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.00</td>
    <td align="right">4.39</td>
    <td align="right">4.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.55</td>
    <td align="right">12.59</td>
    <td align="right">15.99</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.54</td>
    <td align="right">4.36</td>
    <td align="right">4.37</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">7.50</td>
    <td align="right">5.05</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.55</td>
    <td align="right">15.67</td>
    <td align="right">15.26</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.11</td>
    <td align="right">4.95</td>
    <td align="right">5.14</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.06</td>
    <td align="right">5.91</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.34</td>
    <td align="right">20.64</td>
    <td align="right">15.62</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.32</td>
    <td align="right">5.61</td>
    <td align="right">5.78</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.78</td>
    <td align="right">3.22</td>
    <td align="right">3.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.89</td>
    <td align="right">3.38</td>
    <td align="right">3.39</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.00</td>
    <td align="right">3.32</td>
    <td align="right">3.28</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.44</td>
    <td align="right">2.35</td>
    <td align="right">2.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.56</td>
    <td align="right">3.92</td>
    <td align="right">3.92</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.51</td>
    <td align="right">4.21</td>
    <td align="right">4.23</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.02</td>
    <td align="right">2.16</td>
    <td align="right">2.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.43</td>
    <td align="right">6.93</td>
    <td align="right">6.95</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.81</td>
    <td align="right">6.60</td>
    <td align="right">6.61</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.97</td>
    <td align="right">4.17</td>
    <td align="right">3.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.84</td>
    <td align="right">7.35</td>
    <td align="right">7.35</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.08</td>
    <td align="right">7.74</td>
    <td align="right">7.74</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.04</td>
    <td align="right">4.25</td>
    <td align="right">3.01</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.43</td>
    <td align="right">2.18</td>
    <td align="right">2.18</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.40</td>
    <td align="right">3.78</td>
    <td align="right">3.78</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.41</td>
    <td align="right">3.64</td>
    <td align="right">3.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.52</td>
    <td align="right">2.25</td>
    <td align="right">2.28</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.78</td>
    <td align="right">3.52</td>
    <td align="right">3.59</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.61</td>
    <td align="right">3.79</td>
    <td align="right">3.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.02</td>
    <td align="right">4.07</td>
    <td align="right">2.79</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.39</td>
    <td align="right">5.77</td>
    <td align="right">4.51</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.59</td>
    <td align="right">5.77</td>
    <td align="right">4.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.14</td>
    <td align="right">4.19</td>
    <td align="right">2.81</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.38</td>
    <td align="right">6.92</td>
    <td align="right">4.53</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">7.52</td>
    <td align="right">6.79</td>
    <td align="right">4.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.42</td>
    <td align="right">5.63</td>
    <td align="right">11.78</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.12</td>
    <td align="right">7.51</td>
    <td align="right">16.00</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.04</td>
    <td align="right">10.30</td>
    <td align="right">10.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.84</td>
    <td align="right">7.63</td>
    <td align="right">11.85</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">11.71</td>
    <td align="right">9.10</td>
    <td align="right">13.61</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.34</td>
    <td align="right">14.35</td>
    <td align="right">14.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.18</td>
    <td align="right">9.55</td>
    <td align="right">11.59</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.03</td>
    <td align="right">11.94</td>
    <td align="right">14.54</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.41</td>
    <td align="right">16.49</td>
    <td align="right">16.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.30</td>
    <td align="right">11.79</td>
    <td align="right">12.33</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.48</td>
    <td align="right">13.58</td>
    <td align="right">14.14</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">22.18</td>
    <td align="right">22.37</td>
    <td align="right">21.33</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.71</td>
    <td align="right">14.93</td>
    <td align="right">5.62</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.81</td>
    <td align="right">8.82</td>
    <td align="right">15.34</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.17</td>
    <td align="right">4.01</td>
    <td align="right">4.14</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.11</td>
    <td align="right">4.65</td>
    <td align="right">4.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">13.36</td>
    <td align="right">13.08</td>
    <td align="right">16.22</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.01</td>
    <td align="right">6.48</td>
    <td align="right">5.53</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">8.46</td>
    <td align="right">5.24</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">18.92</td>
    <td align="right">16.33</td>
    <td align="right">15.17</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.29</td>
    <td align="right">5.32</td>
    <td align="right">5.56</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.25</td>
    <td align="right">7.15</td>
    <td align="right">6.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">22.87</td>
    <td align="right">27.30</td>
    <td align="right">17.66</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">17.72</td>
    <td align="right">17.53</td>
    <td align="right">11.92</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">3.67</td>
    <td align="right">4.45</td>
    <td align="right">4.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.25</td>
    <td align="right">3.69</td>
    <td align="right">3.69</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.37</td>
    <td align="right">3.64</td>
    <td align="right">3.59</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.75</td>
    <td align="right">2.62</td>
    <td align="right">2.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.70</td>
    <td align="right">4.04</td>
    <td align="right">4.05</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.75</td>
    <td align="right">4.31</td>
    <td align="right">4.43</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.17</td>
    <td align="right">2.24</td>
    <td align="right">2.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">6.98</td>
    <td align="right">7.12</td>
    <td align="right">7.10</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">6.57</td>
    <td align="right">6.89</td>
    <td align="right">6.96</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">4.32</td>
    <td align="right">4.40</td>
    <td align="right">3.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">6.94</td>
    <td align="right">9.22</td>
    <td align="right">9.26</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">7.26</td>
    <td align="right">9.37</td>
    <td align="right">9.54</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">5.97</td>
    <td align="right">6.40</td>
    <td align="right">4.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">2.77</td>
    <td align="right">2.44</td>
    <td align="right">2.44</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">3.83</td>
    <td align="right">4.16</td>
    <td align="right">4.19</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">3.89</td>
    <td align="right">3.99</td>
    <td align="right">3.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.78</td>
    <td align="right">2.49</td>
    <td align="right">2.46</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">2.93</td>
    <td align="right">3.66</td>
    <td align="right">3.69</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">3.92</td>
    <td align="right">4.02</td>
    <td align="right">4.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">4.41</td>
    <td align="right">4.27</td>
    <td align="right">2.97</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.31</td>
    <td align="right">6.83</td>
    <td align="right">6.32</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">6.41</td>
    <td align="right">6.73</td>
    <td align="right">6.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">4.80</td>
    <td align="right">4.65</td>
    <td align="right">3.01</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">6.96</td>
    <td align="right">7.14</td>
    <td align="right">6.85</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.96</td>
    <td align="right">6.99</td>
    <td align="right">6.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">6.97</td>
    <td align="right">6.12</td>
    <td align="right">12.06</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">11.44</td>
    <td align="right">8.10</td>
    <td align="right">16.41</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">12.71</td>
    <td align="right">12.91</td>
    <td align="right">13.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">9.32</td>
    <td align="right">8.03</td>
    <td align="right">11.98</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">12.06</td>
    <td align="right">9.43</td>
    <td align="right">13.81</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">17.05</td>
    <td align="right">17.10</td>
    <td align="right">17.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">11.38</td>
    <td align="right">9.72</td>
    <td align="right">11.60</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">15.74</td>
    <td align="right">12.37</td>
    <td align="right">14.91</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">22.69</td>
    <td align="right">22.75</td>
    <td align="right">22.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">18.65</td>
    <td align="right">13.30</td>
    <td align="right">13.09</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">19.81</td>
    <td align="right">14.41</td>
    <td align="right">14.26</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">30.75</td>
    <td align="right">25.57</td>
    <td align="right">24.71</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">24.11</td>
    <td align="right">7.31</td>
    <td align="right">3.57</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.25</td>
    <td align="right">8.38</td>
    <td align="right">12.79</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.55</td>
    <td align="right">1.29</td>
    <td align="right">1.31</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">2.23</td>
    <td align="right">1.94</td>
    <td align="right">2.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.76</td>
    <td align="right">7.76</td>
    <td align="right">12.81</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.49</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.75</td>
    <td align="right">2.34</td>
    <td align="right">1.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.63</td>
    <td align="right">9.86</td>
    <td align="right">13.16</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.98</td>
    <td align="right">1.87</td>
    <td align="right">1.77</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.96</td>
    <td align="right">1.83</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.66</td>
    <td align="right">13.03</td>
    <td align="right">12.64</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.07</td>
    <td align="right">2.08</td>
    <td align="right">2.55</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.95</td>
    <td align="right">1.86</td>
    <td align="right">2.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.76</td>
    <td align="right">1.99</td>
    <td align="right">2.01</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.48</td>
    <td align="right">1.92</td>
    <td align="right">1.95</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.73</td>
    <td align="right">3.59</td>
    <td align="right">2.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.86</td>
    <td align="right">2.61</td>
    <td align="right">2.76</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.90</td>
    <td align="right">2.63</td>
    <td align="right">3.33</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.91</td>
    <td align="right">2.98</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.55</td>
    <td align="right">3.80</td>
    <td align="right">3.15</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.54</td>
    <td align="right">5.06</td>
    <td align="right">7.40</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.68</td>
    <td align="right">2.95</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.94</td>
    <td align="right">4.20</td>
    <td align="right">4.19</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.20</td>
    <td align="right">4.69</td>
    <td align="right">4.29</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.70</td>
    <td align="right">3.48</td>
    <td align="right">1.98</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.14</td>
    <td align="right">1.78</td>
    <td align="right">1.77</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.63</td>
    <td align="right">2.58</td>
    <td align="right">1.87</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.88</td>
    <td align="right">2.46</td>
    <td align="right">2.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.29</td>
    <td align="right">1.77</td>
    <td align="right">1.83</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.22</td>
    <td align="right">2.18</td>
    <td align="right">2.60</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.25</td>
    <td align="right">2.44</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.20</td>
    <td align="right">2.68</td>
    <td align="right">1.92</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.66</td>
    <td align="right">3.26</td>
    <td align="right">3.11</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.56</td>
    <td align="right">3.80</td>
    <td align="right">4.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.26</td>
    <td align="right">3.30</td>
    <td align="right">3.48</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.07</td>
    <td align="right">3.89</td>
    <td align="right">5.37</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.30</td>
    <td align="right">4.67</td>
    <td align="right">4.38</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">3.54</td>
    <td align="right">4.50</td>
    <td align="right">11.23</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">8.09</td>
    <td align="right">4.33</td>
    <td align="right">13.60</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">8.84</td>
    <td align="right">5.72</td>
    <td align="right">5.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">5.18</td>
    <td align="right">5.21</td>
    <td align="right">12.44</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">9.30</td>
    <td align="right">5.14</td>
    <td align="right">12.62</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">12.59</td>
    <td align="right">7.93</td>
    <td align="right">7.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">6.26</td>
    <td align="right">5.16</td>
    <td align="right">10.37</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">12.05</td>
    <td align="right">6.39</td>
    <td align="right">12.00</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">12.98</td>
    <td align="right">8.95</td>
    <td align="right">9.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">8.63</td>
    <td align="right">8.76</td>
    <td align="right">12.33</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">12.84</td>
    <td align="right">11.18</td>
    <td align="right">12.37</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">18.21</td>
    <td align="right">11.28</td>
    <td align="right">20.47</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.63</td>
    <td align="right">15.62</td>
    <td align="right">10.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.54</td>
    <td align="right">14.35</td>
    <td align="right">21.38</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.43</td>
    <td align="right">3.17</td>
    <td align="right">3.04</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.79</td>
    <td align="right">2.87</td>
    <td align="right">4.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">45.24</td>
    <td align="right">38.21</td>
    <td align="right">32.43</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">11.21</td>
    <td align="right">12.02</td>
    <td align="right">10.43</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.95</td>
    <td align="right">8.65</td>
    <td align="right">11.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">68.95</td>
    <td align="right">55.82</td>
    <td align="right">31.13</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">17.23</td>
    <td align="right">14.25</td>
    <td align="right">14.69</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">13.06</td>
    <td align="right">11.37</td>
    <td align="right">13.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">102.85</td>
    <td align="right">79.42</td>
    <td align="right">34.10</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">17.39</td>
    <td align="right">14.87</td>
    <td align="right">15.24</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.63</td>
    <td align="right">10.21</td>
    <td align="right">9.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.20</td>
    <td align="right">7.57</td>
    <td align="right">7.41</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.86</td>
    <td align="right">9.73</td>
    <td align="right">9.47</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.58</td>
    <td align="right">7.73</td>
    <td align="right">7.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.32</td>
    <td align="right">11.03</td>
    <td align="right">8.81</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.06</td>
    <td align="right">10.84</td>
    <td align="right">15.13</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">9.71</td>
    <td align="right">10.95</td>
    <td align="right">10.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">22.55</td>
    <td align="right">21.54</td>
    <td align="right">21.44</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.76</td>
    <td align="right">18.48</td>
    <td align="right">20.15</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">16.45</td>
    <td align="right">16.86</td>
    <td align="right">12.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">24.85</td>
    <td align="right">16.35</td>
    <td align="right">16.69</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">22.78</td>
    <td align="right">17.34</td>
    <td align="right">17.97</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">11.08</td>
    <td align="right">15.56</td>
    <td align="right">10.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.82</td>
    <td align="right">5.37</td>
    <td align="right">5.26</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.03</td>
    <td align="right">5.86</td>
    <td align="right">6.69</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.10</td>
    <td align="right">5.24</td>
    <td align="right">5.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">4.09</td>
    <td align="right">5.85</td>
    <td align="right">4.93</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">5.48</td>
    <td align="right">5.96</td>
    <td align="right">5.74</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">5.45</td>
    <td align="right">6.66</td>
    <td align="right">6.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">10.00</td>
    <td align="right">9.26</td>
    <td align="right">7.69</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">20.91</td>
    <td align="right">22.45</td>
    <td align="right">14.65</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">15.58</td>
    <td align="right">14.69</td>
    <td align="right">15.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">11.79</td>
    <td align="right">12.92</td>
    <td align="right">9.21</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">18.95</td>
    <td align="right">17.25</td>
    <td align="right">17.77</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.96</td>
    <td align="right">16.27</td>
    <td align="right">17.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.89</td>
    <td align="right">7.74</td>
    <td align="right">14.74</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">14.53</td>
    <td align="right">8.92</td>
    <td align="right">19.04</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">10.11</td>
    <td align="right">10.21</td>
    <td align="right">9.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">16.51</td>
    <td align="right">13.81</td>
    <td align="right">18.84</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">31.64</td>
    <td align="right">21.10</td>
    <td align="right">21.45</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">28.68</td>
    <td align="right">33.54</td>
    <td align="right">33.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">21.28</td>
    <td align="right">18.04</td>
    <td align="right">16.56</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">35.65</td>
    <td align="right">23.08</td>
    <td align="right">19.92</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">39.06</td>
    <td align="right">41.88</td>
    <td align="right">34.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">30.34</td>
    <td align="right">28.16</td>
    <td align="right">17.61</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">46.00</td>
    <td align="right">35.89</td>
    <td align="right">21.66</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">59.62</td>
    <td align="right">57.08</td>
    <td align="right">48.20</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.32</td>
    <td align="right">5.94</td>
    <td align="right">3.75</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.02</td>
    <td align="right">12.44</td>
    <td align="right">16.95</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.82</td>
    <td align="right">4.21</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.96</td>
    <td align="right">5.25</td>
    <td align="right">5.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.40</td>
    <td align="right">17.73</td>
    <td align="right">17.64</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.01</td>
    <td align="right">4.75</td>
    <td align="right">4.79</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.05</td>
    <td align="right">6.07</td>
    <td align="right">5.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.47</td>
    <td align="right">21.20</td>
    <td align="right">16.70</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.59</td>
    <td align="right">5.30</td>
    <td align="right">5.44</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.32</td>
    <td align="right">6.56</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.82</td>
    <td align="right">26.93</td>
    <td align="right">17.47</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.87</td>
    <td align="right">5.87</td>
    <td align="right">5.96</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.43</td>
    <td align="right">7.36</td>
    <td align="right">7.41</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.88</td>
    <td align="right">5.55</td>
    <td align="right">5.56</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.19</td>
    <td align="right">5.62</td>
    <td align="right">5.60</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.34</td>
    <td align="right">3.90</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.64</td>
    <td align="right">8.12</td>
    <td align="right">8.15</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.35</td>
    <td align="right">8.72</td>
    <td align="right">7.88</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.87</td>
    <td align="right">4.85</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.07</td>
    <td align="right">10.99</td>
    <td align="right">10.90</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">24.37</td>
    <td align="right">10.62</td>
    <td align="right">11.01</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.03</td>
    <td align="right">7.13</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">16.78</td>
    <td align="right">12.53</td>
    <td align="right">12.52</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">21.91</td>
    <td align="right">13.48</td>
    <td align="right">13.61</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.05</td>
    <td align="right">7.08</td>
    <td align="right">5.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.24</td>
    <td align="right">3.79</td>
    <td align="right">3.81</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.57</td>
    <td align="right">5.53</td>
    <td align="right">5.53</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.63</td>
    <td align="right">5.42</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.30</td>
    <td align="right">5.54</td>
    <td align="right">4.68</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.79</td>
    <td align="right">5.73</td>
    <td align="right">5.00</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.95</td>
    <td align="right">7.08</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.07</td>
    <td align="right">6.75</td>
    <td align="right">5.02</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.84</td>
    <td align="right">9.24</td>
    <td align="right">7.59</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.62</td>
    <td align="right">9.22</td>
    <td align="right">7.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.15</td>
    <td align="right">6.90</td>
    <td align="right">5.02</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.34</td>
    <td align="right">10.75</td>
    <td align="right">7.70</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.16</td>
    <td align="right">10.53</td>
    <td align="right">7.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.71</td>
    <td align="right">8.64</td>
    <td align="right">13.69</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.36</td>
    <td align="right">11.72</td>
    <td align="right">17.13</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">12.84</td>
    <td align="right">10.82</td>
    <td align="right">10.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.76</td>
    <td align="right">10.98</td>
    <td align="right">12.93</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.57</td>
    <td align="right">13.17</td>
    <td align="right">14.50</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">17.78</td>
    <td align="right">16.07</td>
    <td align="right">15.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.40</td>
    <td align="right">14.30</td>
    <td align="right">12.72</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">19.05</td>
    <td align="right">17.70</td>
    <td align="right">15.32</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">21.95</td>
    <td align="right">18.90</td>
    <td align="right">18.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.37</td>
    <td align="right">17.55</td>
    <td align="right">14.03</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">20.70</td>
    <td align="right">20.58</td>
    <td align="right">14.84</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">29.04</td>
    <td align="right">26.95</td>
    <td align="right">28.18</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">39.78</td>
    <td align="right">20.31</td>
    <td align="right">8.14</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.43</td>
    <td align="right">12.97</td>
    <td align="right">17.61</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.05</td>
    <td align="right">4.50</td>
    <td align="right">4.48</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.89</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">21.98</td>
    <td align="right">18.70</td>
    <td align="right">18.48</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.57</td>
    <td align="right">5.10</td>
    <td align="right">5.12</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.20</td>
    <td align="right">6.35</td>
    <td align="right">6.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">27.65</td>
    <td align="right">23.39</td>
    <td align="right">17.24</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.95</td>
    <td align="right">5.77</td>
    <td align="right">5.70</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.42</td>
    <td align="right">7.09</td>
    <td align="right">7.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">40.24</td>
    <td align="right">37.69</td>
    <td align="right">19.71</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">14.58</td>
    <td align="right">10.12</td>
    <td align="right">9.97</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.96</td>
    <td align="right">9.71</td>
    <td align="right">9.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.31</td>
    <td align="right">6.25</td>
    <td align="right">6.26</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.40</td>
    <td align="right">6.31</td>
    <td align="right">6.27</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.72</td>
    <td align="right">4.15</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.70</td>
    <td align="right">9.47</td>
    <td align="right">9.52</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.99</td>
    <td align="right">9.32</td>
    <td align="right">8.63</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.36</td>
    <td align="right">5.23</td>
    <td align="right">4.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">16.62</td>
    <td align="right">13.64</td>
    <td align="right">13.47</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">24.97</td>
    <td align="right">11.52</td>
    <td align="right">11.56</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.82</td>
    <td align="right">7.74</td>
    <td align="right">5.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">19.72</td>
    <td align="right">15.25</td>
    <td align="right">15.41</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">25.38</td>
    <td align="right">16.38</td>
    <td align="right">16.40</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">8.29</td>
    <td align="right">10.79</td>
    <td align="right">8.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.64</td>
    <td align="right">4.09</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.07</td>
    <td align="right">5.92</td>
    <td align="right">5.92</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.22</td>
    <td align="right">5.75</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.76</td>
    <td align="right">5.95</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.32</td>
    <td align="right">6.27</td>
    <td align="right">5.42</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.52</td>
    <td align="right">7.63</td>
    <td align="right">6.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.93</td>
    <td align="right">7.48</td>
    <td align="right">5.58</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.70</td>
    <td align="right">10.29</td>
    <td align="right">8.39</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.55</td>
    <td align="right">10.09</td>
    <td align="right">8.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.93</td>
    <td align="right">12.82</td>
    <td align="right">10.01</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">12.67</td>
    <td align="right">14.02</td>
    <td align="right">10.37</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">12.35</td>
    <td align="right">12.15</td>
    <td align="right">8.93</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">9.71</td>
    <td align="right">9.63</td>
    <td align="right">13.96</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.73</td>
    <td align="right">12.65</td>
    <td align="right">17.61</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">16.37</td>
    <td align="right">14.46</td>
    <td align="right">14.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">13.82</td>
    <td align="right">12.13</td>
    <td align="right">13.37</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">14.13</td>
    <td align="right">14.18</td>
    <td align="right">14.96</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">21.63</td>
    <td align="right">20.32</td>
    <td align="right">20.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">16.87</td>
    <td align="right">16.08</td>
    <td align="right">13.31</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">22.47</td>
    <td align="right">19.90</td>
    <td align="right">16.08</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">28.45</td>
    <td align="right">21.73</td>
    <td align="right">23.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">23.84</td>
    <td align="right">21.56</td>
    <td align="right">15.42</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">24.90</td>
    <td align="right">24.69</td>
    <td align="right">15.95</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">34.83</td>
    <td align="right">32.80</td>
    <td align="right">32.90</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">64.71</td>
    <td align="right">33.94</td>
    <td align="right">18.73</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.74</td>
    <td align="right">42.25</td>
    <td align="right">36.38</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.60</td>
    <td align="right">15.64</td>
    <td align="right">15.63</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.29</td>
    <td align="right">19.16</td>
    <td align="right">19.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.80</td>
    <td align="right">65.20</td>
    <td align="right">39.44</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.43</td>
    <td align="right">19.64</td>
    <td align="right">19.60</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">17.06</td>
    <td align="right">18.72</td>
    <td align="right">18.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.55</td>
    <td align="right">79.34</td>
    <td align="right">38.93</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.67</td>
    <td align="right">18.65</td>
    <td align="right">18.72</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.29</td>
    <td align="right">18.36</td>
    <td align="right">18.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">57.82</td>
    <td align="right">98.78</td>
    <td align="right">37.50</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.51</td>
    <td align="right">18.86</td>
    <td align="right">18.89</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.12</td>
    <td align="right">20.02</td>
    <td align="right">20.20</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.41</td>
    <td align="right">21.22</td>
    <td align="right">21.29</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.97</td>
    <td align="right">22.46</td>
    <td align="right">22.40</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">11.08</td>
    <td align="right">13.75</td>
    <td align="right">13.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.68</td>
    <td align="right">26.25</td>
    <td align="right">26.24</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">40.22</td>
    <td align="right">28.19</td>
    <td align="right">27.92</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">13.26</td>
    <td align="right">16.55</td>
    <td align="right">16.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.49</td>
    <td align="right">33.58</td>
    <td align="right">33.51</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.76</td>
    <td align="right">46.90</td>
    <td align="right">47.28</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">15.07</td>
    <td align="right">19.78</td>
    <td align="right">19.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">35.08</td>
    <td align="right">36.60</td>
    <td align="right">36.66</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">78.29</td>
    <td align="right">56.85</td>
    <td align="right">56.99</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.12</td>
    <td align="right">25.64</td>
    <td align="right">25.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">15.44</td>
    <td align="right">15.73</td>
    <td align="right">15.70</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.36</td>
    <td align="right">21.30</td>
    <td align="right">21.37</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.81</td>
    <td align="right">22.30</td>
    <td align="right">22.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">20.00</td>
    <td align="right">20.55</td>
    <td align="right">20.65</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.56</td>
    <td align="right">26.13</td>
    <td align="right">26.09</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">40.05</td>
    <td align="right">27.94</td>
    <td align="right">27.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.70</td>
    <td align="right">24.94</td>
    <td align="right">24.92</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.44</td>
    <td align="right">33.30</td>
    <td align="right">33.47</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.46</td>
    <td align="right">47.01</td>
    <td align="right">47.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.62</td>
    <td align="right">37.57</td>
    <td align="right">37.55</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.94</td>
    <td align="right">36.54</td>
    <td align="right">36.42</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">78.01</td>
    <td align="right">56.72</td>
    <td align="right">56.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.30</td>
    <td align="right">20.88</td>
    <td align="right">25.56</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.61</td>
    <td align="right">29.31</td>
    <td align="right">34.66</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">28.62</td>
    <td align="right">30.92</td>
    <td align="right">30.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.30</td>
    <td align="right">28.47</td>
    <td align="right">26.37</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">39.20</td>
    <td align="right">33.63</td>
    <td align="right">30.76</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">38.05</td>
    <td align="right">39.32</td>
    <td align="right">39.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.78</td>
    <td align="right">33.81</td>
    <td align="right">25.83</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">47.42</td>
    <td align="right">42.18</td>
    <td align="right">33.86</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.88</td>
    <td align="right">42.04</td>
    <td align="right">41.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.90</td>
    <td align="right">40.53</td>
    <td align="right">27.07</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">50.28</td>
    <td align="right">44.38</td>
    <td align="right">31.53</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">54.44</td>
    <td align="right">58.86</td>
    <td align="right">58.91</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">100.46</td>
    <td align="right">125.06</td>
    <td align="right">31.36</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">30.28</td>
    <td align="right">46.91</td>
    <td align="right">41.04</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.58</td>
    <td align="right">16.48</td>
    <td align="right">16.56</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">21.51</td>
    <td align="right">31.20</td>
    <td align="right">23.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">75.55</td>
    <td align="right">115.29</td>
    <td align="right">60.31</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">44.47</td>
    <td align="right">52.92</td>
    <td align="right">48.29</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">41.15</td>
    <td align="right">51.37</td>
    <td align="right">52.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">109.21</td>
    <td align="right">203.38</td>
    <td align="right">65.39</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">36.40</td>
    <td align="right">38.42</td>
    <td align="right">36.77</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">53.20</td>
    <td align="right">56.68</td>
    <td align="right">51.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">246.89</td>
    <td align="right">382.29</td>
    <td align="right">111.04</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">47.50</td>
    <td align="right">58.87</td>
    <td align="right">53.17</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">43.38</td>
    <td align="right">53.26</td>
    <td align="right">61.33</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.62</td>
    <td align="right">32.09</td>
    <td align="right">33.45</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">46.30</td>
    <td align="right">25.74</td>
    <td align="right">26.56</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">12.04</td>
    <td align="right">15.67</td>
    <td align="right">15.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">26.44</td>
    <td align="right">32.30</td>
    <td align="right">34.33</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">56.45</td>
    <td align="right">58.56</td>
    <td align="right">54.24</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">17.40</td>
    <td align="right">19.65</td>
    <td align="right">19.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">69.54</td>
    <td align="right">86.49</td>
    <td align="right">85.60</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">117.54</td>
    <td align="right">100.08</td>
    <td align="right">103.34</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">54.90</td>
    <td align="right">54.57</td>
    <td align="right">54.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">95.76</td>
    <td align="right">105.61</td>
    <td align="right">107.75</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">139.34</td>
    <td align="right">116.14</td>
    <td align="right">91.62</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">63.96</td>
    <td align="right">89.43</td>
    <td align="right">72.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.91</td>
    <td align="right">18.27</td>
    <td align="right">18.00</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">27.36</td>
    <td align="right">24.16</td>
    <td align="right">23.07</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">44.02</td>
    <td align="right">29.91</td>
    <td align="right">27.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">37.56</td>
    <td align="right">35.58</td>
    <td align="right">21.75</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">22.82</td>
    <td align="right">25.54</td>
    <td align="right">25.74</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">46.69</td>
    <td align="right">31.81</td>
    <td align="right">34.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.35</td>
    <td align="right">33.83</td>
    <td align="right">33.10</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.46</td>
    <td align="right">57.71</td>
    <td align="right">55.16</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">72.40</td>
    <td align="right">54.16</td>
    <td align="right">60.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">90.70</td>
    <td align="right">87.58</td>
    <td align="right">93.51</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">82.96</td>
    <td align="right">97.64</td>
    <td align="right">101.57</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">127.68</td>
    <td align="right">99.17</td>
    <td align="right">69.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">17.78</td>
    <td align="right">22.11</td>
    <td align="right">26.78</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">32.81</td>
    <td align="right">31.03</td>
    <td align="right">35.94</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">29.36</td>
    <td align="right">32.64</td>
    <td align="right">32.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">27.69</td>
    <td align="right">30.49</td>
    <td align="right">29.31</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">52.66</td>
    <td align="right">43.81</td>
    <td align="right">30.52</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">38.96</td>
    <td align="right">40.75</td>
    <td align="right">40.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">41.02</td>
    <td align="right">53.25</td>
    <td align="right">35.41</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">61.46</td>
    <td align="right">78.13</td>
    <td align="right">46.22</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">58.86</td>
    <td align="right">46.43</td>
    <td align="right">47.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">90.24</td>
    <td align="right">102.70</td>
    <td align="right">56.04</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">134.81</td>
    <td align="right">132.80</td>
    <td align="right">74.20</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">108.07</td>
    <td align="right">103.38</td>
    <td align="right">117.60</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.79</td>
    <td align="right">10.34</td>
    <td align="right">7.92</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">14.00</td>
    <td align="right">22.87</td>
    <td align="right">26.64</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">10.30</td>
    <td align="right">12.33</td>
    <td align="right">12.35</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">28.75</td>
    <td align="right">13.96</td>
    <td align="right">13.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.51</td>
    <td align="right">35.24</td>
    <td align="right">29.25</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">31.16</td>
    <td align="right">14.09</td>
    <td align="right">14.11</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">14.74</td>
    <td align="right">15.23</td>
    <td align="right">15.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.31</td>
    <td align="right">47.41</td>
    <td align="right">29.38</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">14.79</td>
    <td align="right">15.44</td>
    <td align="right">15.34</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">16.28</td>
    <td align="right">16.76</td>
    <td align="right">16.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.68</td>
    <td align="right">60.52</td>
    <td align="right">31.02</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">16.32</td>
    <td align="right">16.29</td>
    <td align="right">16.26</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">17.44</td>
    <td align="right">17.85</td>
    <td align="right">17.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.78</td>
    <td align="right">16.15</td>
    <td align="right">16.10</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.23</td>
    <td align="right">16.56</td>
    <td align="right">16.54</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.00</td>
    <td align="right">9.33</td>
    <td align="right">9.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.34</td>
    <td align="right">22.44</td>
    <td align="right">22.46</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.76</td>
    <td align="right">22.38</td>
    <td align="right">22.46</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.57</td>
    <td align="right">14.07</td>
    <td align="right">14.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.09</td>
    <td align="right">32.00</td>
    <td align="right">32.09</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.60</td>
    <td align="right">30.72</td>
    <td align="right">30.78</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.47</td>
    <td align="right">17.56</td>
    <td align="right">17.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.90</td>
    <td align="right">35.70</td>
    <td align="right">35.67</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.88</td>
    <td align="right">35.69</td>
    <td align="right">35.79</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.37</td>
    <td align="right">20.48</td>
    <td align="right">20.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.54</td>
    <td align="right">9.35</td>
    <td align="right">9.36</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.79</td>
    <td align="right">16.07</td>
    <td align="right">16.09</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.32</td>
    <td align="right">16.63</td>
    <td align="right">16.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">12.11</td>
    <td align="right">13.71</td>
    <td align="right">13.70</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.36</td>
    <td align="right">22.44</td>
    <td align="right">22.48</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.79</td>
    <td align="right">22.33</td>
    <td align="right">22.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.08</td>
    <td align="right">17.60</td>
    <td align="right">17.65</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.10</td>
    <td align="right">32.00</td>
    <td align="right">32.05</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.58</td>
    <td align="right">30.68</td>
    <td align="right">30.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.04</td>
    <td align="right">21.08</td>
    <td align="right">20.92</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.93</td>
    <td align="right">35.78</td>
    <td align="right">35.72</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.91</td>
    <td align="right">35.95</td>
    <td align="right">35.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">12.97</td>
    <td align="right">16.16</td>
    <td align="right">19.88</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.28</td>
    <td align="right">33.77</td>
    <td align="right">38.42</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">20.62</td>
    <td align="right">24.24</td>
    <td align="right">24.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.73</td>
    <td align="right">23.49</td>
    <td align="right">20.60</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">54.22</td>
    <td align="right">37.33</td>
    <td align="right">35.91</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">27.04</td>
    <td align="right">31.85</td>
    <td align="right">31.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">23.90</td>
    <td align="right">29.91</td>
    <td align="right">20.46</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">60.49</td>
    <td align="right">45.94</td>
    <td align="right">38.28</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">30.85</td>
    <td align="right">35.25</td>
    <td align="right">35.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">29.87</td>
    <td align="right">35.48</td>
    <td align="right">21.27</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">67.80</td>
    <td align="right">48.06</td>
    <td align="right">37.66</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">41.82</td>
    <td align="right">46.03</td>
    <td align="right">45.97</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">98.31</td>
    <td align="right">51.11</td>
    <td align="right">11.78</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.43</td>
    <td align="right">23.41</td>
    <td align="right">28.66</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">11.73</td>
    <td align="right">13.02</td>
    <td align="right">12.55</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">32.50</td>
    <td align="right">14.69</td>
    <td align="right">14.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">21.50</td>
    <td align="right">38.19</td>
    <td align="right">30.63</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">35.78</td>
    <td align="right">15.16</td>
    <td align="right">14.85</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">17.06</td>
    <td align="right">19.49</td>
    <td align="right">20.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">27.77</td>
    <td align="right">62.51</td>
    <td align="right">33.48</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">23.65</td>
    <td align="right">43.34</td>
    <td align="right">38.44</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">29.84</td>
    <td align="right">38.95</td>
    <td align="right">28.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">61.70</td>
    <td align="right">117.53</td>
    <td align="right">47.44</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">31.40</td>
    <td align="right">32.90</td>
    <td align="right">38.81</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">38.31</td>
    <td align="right">38.33</td>
    <td align="right">30.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.03</td>
    <td align="right">17.55</td>
    <td align="right">17.34</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.53</td>
    <td align="right">17.81</td>
    <td align="right">17.83</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.23</td>
    <td align="right">9.54</td>
    <td align="right">9.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.72</td>
    <td align="right">26.57</td>
    <td align="right">26.65</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">21.44</td>
    <td align="right">23.71</td>
    <td align="right">28.41</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.25</td>
    <td align="right">16.10</td>
    <td align="right">15.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">52.02</td>
    <td align="right">58.07</td>
    <td align="right">60.88</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">42.29</td>
    <td align="right">44.48</td>
    <td align="right">41.86</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">21.46</td>
    <td align="right">29.80</td>
    <td align="right">28.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">48.00</td>
    <td align="right">70.93</td>
    <td align="right">68.08</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">62.16</td>
    <td align="right">77.57</td>
    <td align="right">69.34</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">40.10</td>
    <td align="right">46.25</td>
    <td align="right">48.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.76</td>
    <td align="right">9.93</td>
    <td align="right">9.71</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">14.19</td>
    <td align="right">18.74</td>
    <td align="right">17.32</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.63</td>
    <td align="right">17.69</td>
    <td align="right">17.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">14.97</td>
    <td align="right">17.30</td>
    <td align="right">18.06</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">19.32</td>
    <td align="right">26.41</td>
    <td align="right">26.27</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">26.01</td>
    <td align="right">34.05</td>
    <td align="right">32.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">25.76</td>
    <td align="right">44.37</td>
    <td align="right">38.86</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">52.60</td>
    <td align="right">69.92</td>
    <td align="right">72.20</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">64.52</td>
    <td align="right">71.70</td>
    <td align="right">57.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">49.26</td>
    <td align="right">52.94</td>
    <td align="right">52.10</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">65.36</td>
    <td align="right">73.04</td>
    <td align="right">78.75</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">79.84</td>
    <td align="right">81.71</td>
    <td align="right">86.89</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">15.23</td>
    <td align="right">18.01</td>
    <td align="right">22.06</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">50.78</td>
    <td align="right">39.48</td>
    <td align="right">41.48</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">21.89</td>
    <td align="right">26.03</td>
    <td align="right">25.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">25.95</td>
    <td align="right">27.63</td>
    <td align="right">23.25</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">66.26</td>
    <td align="right">42.91</td>
    <td align="right">41.10</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">28.65</td>
    <td align="right">33.52</td>
    <td align="right">33.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">31.92</td>
    <td align="right">48.01</td>
    <td align="right">26.54</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">100.67</td>
    <td align="right">70.94</td>
    <td align="right">51.36</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">34.08</td>
    <td align="right">37.97</td>
    <td align="right">37.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">56.32</td>
    <td align="right">66.92</td>
    <td align="right">30.78</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">110.76</td>
    <td align="right">123.68</td>
    <td align="right">75.97</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">77.92</td>
    <td align="right">69.82</td>
    <td align="right">67.05</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">48.44</td>
    <td align="right">17.79</td>
    <td align="right">8.82</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">60.19</td>
    <td align="right">55.19</td>
    <td align="right">41.73</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.14</td>
    <td align="right">19.76</td>
    <td align="right">23.54</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">23.25</td>
    <td align="right">21.67</td>
    <td align="right">24.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">90.87</td>
    <td align="right">81.19</td>
    <td align="right">44.32</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.54</td>
    <td align="right">21.47</td>
    <td align="right">24.00</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.49</td>
    <td align="right">22.55</td>
    <td align="right">24.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">112.11</td>
    <td align="right">101.92</td>
    <td align="right">44.80</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.61</td>
    <td align="right">23.05</td>
    <td align="right">24.66</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">28.19</td>
    <td align="right">24.54</td>
    <td align="right">25.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">143.01</td>
    <td align="right">128.46</td>
    <td align="right">45.75</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.91</td>
    <td align="right">24.71</td>
    <td align="right">25.74</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">30.64</td>
    <td align="right">25.93</td>
    <td align="right">26.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">23.14</td>
    <td align="right">41.51</td>
    <td align="right">41.63</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">28.94</td>
    <td align="right">41.87</td>
    <td align="right">41.41</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.82</td>
    <td align="right">25.73</td>
    <td align="right">25.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.83</td>
    <td align="right">57.08</td>
    <td align="right">57.37</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">34.08</td>
    <td align="right">58.54</td>
    <td align="right">58.31</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.91</td>
    <td align="right">36.74</td>
    <td align="right">26.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.79</td>
    <td align="right">77.25</td>
    <td align="right">77.50</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.80</td>
    <td align="right">78.46</td>
    <td align="right">78.45</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.73</td>
    <td align="right">58.31</td>
    <td align="right">41.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.30</td>
    <td align="right">86.97</td>
    <td align="right">87.07</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">51.48</td>
    <td align="right">93.21</td>
    <td align="right">93.51</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">30.08</td>
    <td align="right">60.28</td>
    <td align="right">42.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">19.22</td>
    <td align="right">26.35</td>
    <td align="right">26.24</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.98</td>
    <td align="right">29.41</td>
    <td align="right">29.42</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">21.12</td>
    <td align="right">31.16</td>
    <td align="right">31.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">19.25</td>
    <td align="right">46.89</td>
    <td align="right">35.64</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.83</td>
    <td align="right">40.61</td>
    <td align="right">28.38</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.41</td>
    <td align="right">53.01</td>
    <td align="right">40.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">29.44</td>
    <td align="right">57.60</td>
    <td align="right">39.87</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.43</td>
    <td align="right">53.72</td>
    <td align="right">35.36</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.64</td>
    <td align="right">62.50</td>
    <td align="right">44.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">30.21</td>
    <td align="right">60.42</td>
    <td align="right">42.49</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">34.04</td>
    <td align="right">65.77</td>
    <td align="right">45.14</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.65</td>
    <td align="right">65.77</td>
    <td align="right">45.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.39</td>
    <td align="right">42.98</td>
    <td align="right">35.16</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.88</td>
    <td align="right">53.74</td>
    <td align="right">40.58</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">37.17</td>
    <td align="right">60.13</td>
    <td align="right">60.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">36.66</td>
    <td align="right">60.94</td>
    <td align="right">35.69</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">42.36</td>
    <td align="right">61.56</td>
    <td align="right">38.34</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">46.40</td>
    <td align="right">77.71</td>
    <td align="right">77.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">42.13</td>
    <td align="right">76.27</td>
    <td align="right">36.55</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">51.17</td>
    <td align="right">82.99</td>
    <td align="right">40.19</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">48.93</td>
    <td align="right">83.93</td>
    <td align="right">84.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">56.48</td>
    <td align="right">99.82</td>
    <td align="right">37.85</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">59.58</td>
    <td align="right">96.89</td>
    <td align="right">39.80</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">68.21</td>
    <td align="right">119.90</td>
    <td align="right">120.29</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.77</td>
    <td align="right">40.20</td>
    <td align="right">24.75</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">145.00</td>
    <td align="right">119.25</td>
    <td align="right">63.49</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">48.88</td>
    <td align="right">44.68</td>
    <td align="right">51.59</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">71.03</td>
    <td align="right">41.63</td>
    <td align="right">46.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">296.31</td>
    <td align="right">259.25</td>
    <td align="right">106.27</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">88.02</td>
    <td align="right">60.13</td>
    <td align="right">58.71</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">105.64</td>
    <td align="right">57.49</td>
    <td align="right">60.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">436.87</td>
    <td align="right">355.42</td>
    <td align="right">112.58</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">100.20</td>
    <td align="right">64.04</td>
    <td align="right">61.50</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">100.69</td>
    <td align="right">59.56</td>
    <td align="right">64.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">574.94</td>
    <td align="right">456.96</td>
    <td align="right">122.18</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">111.87</td>
    <td align="right">67.15</td>
    <td align="right">66.54</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">81.98</td>
    <td align="right">59.38</td>
    <td align="right">66.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">38.90</td>
    <td align="right">45.83</td>
    <td align="right">44.12</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.42</td>
    <td align="right">43.83</td>
    <td align="right">43.44</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">19.96</td>
    <td align="right">30.10</td>
    <td align="right">30.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">35.49</td>
    <td align="right">69.50</td>
    <td align="right">84.34</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">79.51</td>
    <td align="right">92.29</td>
    <td align="right">72.70</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.20</td>
    <td align="right">40.99</td>
    <td align="right">29.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">44.71</td>
    <td align="right">82.23</td>
    <td align="right">84.84</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">51.17</td>
    <td align="right">82.73</td>
    <td align="right">87.27</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">57.29</td>
    <td align="right">92.99</td>
    <td align="right">50.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">51.90</td>
    <td align="right">102.70</td>
    <td align="right">103.52</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">73.20</td>
    <td align="right">112.64</td>
    <td align="right">115.36</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">75.10</td>
    <td align="right">108.03</td>
    <td align="right">103.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">20.45</td>
    <td align="right">32.96</td>
    <td align="right">31.88</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">22.21</td>
    <td align="right">36.93</td>
    <td align="right">37.87</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">23.32</td>
    <td align="right">39.52</td>
    <td align="right">36.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">23.29</td>
    <td align="right">62.52</td>
    <td align="right">39.63</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.61</td>
    <td align="right">43.21</td>
    <td align="right">30.33</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">23.88</td>
    <td align="right">60.35</td>
    <td align="right">46.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">33.12</td>
    <td align="right">66.10</td>
    <td align="right">47.74</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">38.88</td>
    <td align="right">62.43</td>
    <td align="right">52.08</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">50.40</td>
    <td align="right">81.93</td>
    <td align="right">79.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">71.75</td>
    <td align="right">122.18</td>
    <td align="right">94.84</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">50.52</td>
    <td align="right">108.64</td>
    <td align="right">101.63</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">50.42</td>
    <td align="right">105.82</td>
    <td align="right">81.00</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">27.93</td>
    <td align="right">52.08</td>
    <td align="right">40.86</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">39.55</td>
    <td align="right">74.08</td>
    <td align="right">47.00</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">41.20</td>
    <td align="right">61.48</td>
    <td align="right">63.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">66.85</td>
    <td align="right">82.82</td>
    <td align="right">41.83</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">89.80</td>
    <td align="right">67.12</td>
    <td align="right">41.30</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">48.28</td>
    <td align="right">78.97</td>
    <td align="right">79.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">48.51</td>
    <td align="right">78.58</td>
    <td align="right">39.88</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">79.40</td>
    <td align="right">89.37</td>
    <td align="right">46.45</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">53.17</td>
    <td align="right">86.35</td>
    <td align="right">86.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">65.59</td>
    <td align="right">107.09</td>
    <td align="right">45.95</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">82.18</td>
    <td align="right">117.21</td>
    <td align="right">55.65</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">76.52</td>
    <td align="right">126.26</td>
    <td align="right">126.14</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
